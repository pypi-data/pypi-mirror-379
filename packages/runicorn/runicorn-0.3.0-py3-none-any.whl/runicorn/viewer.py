from __future__ import annotations

import asyncio
import csv
import json
import logging
import os
import re
import shutil
import time
import psutil
from dataclasses import asdict, dataclass
import tarfile
import zipfile
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple

import aiofiles
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, Body, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .config import get_user_root_dir, set_user_root_dir

from .sdk import DEFAULT_DIRNAME, _default_storage_dir
from . import ssh_sync

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Import new modules if available
try:
    from .experiment import ExperimentManager
    HAS_EXPERIMENT_MANAGER = True
except ImportError:
    ExperimentManager = None
    HAS_EXPERIMENT_MANAGER = False
    logger.debug("ExperimentManager not available")

try:
    from .exporters import MetricsExporter
    HAS_EXPORTER = True
except ImportError:
    MetricsExporter = None
    HAS_EXPORTER = False
    logger.debug("MetricsExporter not available")

# ---------------- API models (module-level to avoid Pydantic forward-ref issues) ----------------

class SSHConnectBody(BaseModel):
    host: str
    port: Optional[int] = 22
    username: str
    password: Optional[str] = None
    pkey: Optional[str] = None  # private key content
    pkey_path: Optional[str] = None
    passphrase: Optional[str] = None
    use_agent: Optional[bool] = True


class SSHCloseBody(BaseModel):
    session_id: str


class SSHMirrorStartBody(BaseModel):
    session_id: str
    remote_root: str
    interval: Optional[float] = 2.0


class SSHMirrorStopBody(BaseModel):
    task_id: str


# ---------------- Storage helpers ----------------

def _ts() -> float:
    return time.time()


def _storage_root(storage: Optional[str]) -> Path:
    root = _default_storage_dir(storage)
    root.mkdir(parents=True, exist_ok=True)
    (root / "runs").mkdir(parents=True, exist_ok=True)
    return root


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def _is_process_alive(pid: Optional[int]) -> bool:
    """Check if a process is still running."""
    if pid is None:
        return False
    try:
        return psutil.pid_exists(pid)
    except Exception:
        # Fallback to basic method if psutil is not available
        try:
            if os.name == 'nt':  # Windows
                import subprocess
                result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], 
                                      capture_output=True, text=True, timeout=5)
                return str(pid) in result.stdout
            else:  # Unix/Linux
                os.kill(pid, 0)  # Signal 0 just checks if process exists
                return True
        except (OSError, subprocess.SubprocessError, ProcessLookupError):
            return False
        except Exception:
            return False

def _update_status_if_process_dead(run_dir: Path) -> None:
    """Update run status to 'failed' if the process is no longer running."""
    try:
        meta_path = run_dir / "meta.json"
        status_path = run_dir / "status.json"
        
        if not meta_path.exists() or not status_path.exists():
            return
        
        meta = _read_json(meta_path)
        status = _read_json(status_path)
        
        # Only check if status is currently "running"
        if status.get("status") != "running":
            return
        
        pid = meta.get("pid")
        if pid and not _is_process_alive(pid):
            # Process is dead, mark as failed
            status.update({
                "status": "failed",
                "ended_at": _ts(),
                "exit_reason": "process_not_found"
            })
            status_path.write_text(
                json.dumps(status, ensure_ascii=False, indent=2), 
                encoding="utf-8"
            )
            logger.info(f"Run {run_dir.name} marked as failed (PID {pid} not found)")
    except Exception as e:
        logger.debug(f"Failed to update status for {run_dir.name}: {e}")

async def _periodic_status_check(root: Path) -> None:
    """Periodically check and update status of running experiments."""
    while True:
        try:
            # Check all running experiments
            for e in _iter_all_runs(root):
                d = e.dir
                status = _read_json(d / "status.json")
                if status.get("status") == "running":
                    _update_status_if_process_dead(d)
            
            # Wait 30 seconds before next check
            await asyncio.sleep(30)
        except asyncio.CancelledError:
            logger.info("Status check task cancelled")
            break
        except Exception as e:
            logger.error(f"Status check task error: {e}")
            await asyncio.sleep(30)  # Continue checking despite errors

def _setup_logging() -> None:
    """Setup logging configuration for the viewer module."""
    # Configure logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Add console handler if not already configured
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)


def _list_run_dirs_legacy(root: Path) -> List[Path]:
    runs_dir = root / "runs"
    if not runs_dir.exists():
        return []
    return sorted([p for p in runs_dir.iterdir() if p.is_dir()], key=lambda p: p.stat().st_mtime, reverse=True)


@dataclass
class RunEntry:
    project: Optional[str]
    name: Optional[str]
    dir: Path


def _is_run_deleted(run_dir: Path) -> bool:
    """Check if a run is marked as deleted."""
    return (run_dir / ".deleted").exists()

def _soft_delete_run(run_dir: Path, reason: str = "user_deleted") -> bool:
    """Mark a run as deleted by creating .deleted marker file."""
    try:
        deleted_info = {
            "deleted_at": _ts(),
            "reason": reason,
            "original_status": _read_json(run_dir / "status.json").get("status", "unknown")
        }
        deleted_file = run_dir / ".deleted"
        deleted_file.write_text(json.dumps(deleted_info, ensure_ascii=False, indent=2), encoding="utf-8")
        logger.info(f"Soft deleted run: {run_dir.name}")
        return True
    except Exception as e:
        logger.error(f"Failed to soft delete run {run_dir.name}: {e}")
        return False

def _restore_run(run_dir: Path) -> bool:
    """Restore a soft-deleted run by removing .deleted marker."""
    try:
        deleted_file = run_dir / ".deleted"
        if deleted_file.exists():
            deleted_file.unlink()
            logger.info(f"Restored run: {run_dir.name}")
            return True
        return False
    except Exception as e:
        logger.error(f"Failed to restore run {run_dir.name}: {e}")
        return False

def _iter_all_runs(root: Path, include_deleted: bool = False) -> List[RunEntry]:
    """Discover runs in both new and legacy layouts.

    New:   root/<project>/<name>/runs/<run_id>
    Legacy:root/runs/<run_id>
    
    Args:
        include_deleted: If False, filter out soft-deleted runs
    """
    entries: List[RunEntry] = []
    # New layout: project/name/runs/*
    try:
        for proj in sorted([p for p in root.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
            # skip well-known non-project dirs
            if proj.name in {"runs", "webui"}:
                continue
            for name in sorted([n for n in proj.iterdir() if n.is_dir()], key=lambda p: p.name.lower()):
                runs_dir = name / "runs"
                if not runs_dir.exists():
                    continue
                for rd in sorted([p for p in runs_dir.iterdir() if p.is_dir()], key=lambda p: p.stat().st_mtime, reverse=True):
                    # Filter out soft-deleted runs unless explicitly requested
                    if not include_deleted and _is_run_deleted(rd):
                        continue
                    entries.append(RunEntry(project=proj.name, name=name.name, dir=rd))
    except Exception:
        pass
    # Legacy layout fallback
    try:
        for rd in _list_run_dirs_legacy(root):
            # Filter out soft-deleted runs unless explicitly requested
            if not include_deleted and _is_run_deleted(rd):
                continue
            # project/name can be inferred from meta.json if present; leave None here
            entries.append(RunEntry(project=None, name=None, dir=rd))
    except Exception:
        pass
    return entries


def _find_run_dir_by_id(root: Path, run_id: str, include_deleted: bool = False) -> Optional[RunEntry]:
    for e in _iter_all_runs(root, include_deleted=include_deleted):
        if e.dir.name == run_id:
            return e
    return None


# ---------------- API schemas ----------------

class RunListItem(BaseModel):
    id: str
    run_dir: Optional[str]
    created_time: Optional[float]
    status: str
    pid: Optional[int] = None
    best_metric_value: Optional[float] = None
    best_metric_name: Optional[str] = None
    project: Optional[str] = None
    name: Optional[str] = None


# ---------------- Metrics extraction ----------------

def _iter_events(events_path: Path) -> Iterator[Dict[str, Any]]:
    if not events_path.exists():
        return
    try:
        with open(events_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue
    except Exception:
        return

# Epoch-based aggregation removed: metrics are tracked only by step/time.


def _aggregate_step_metrics(events_path: Path) -> Tuple[List[str], List[Dict[str, Any]]]:
    """Aggregate step metrics from events file, handling NaN and Inf values."""
    import math
    
    def sanitize_value(v):
        """Convert NaN/Inf to None for JSON compatibility."""
        if isinstance(v, float):
            if math.isnan(v) or math.isinf(v):
                return None
        return v
    
    # Use 'global_step' if present; otherwise fall back to 'step'.
    # Merge multiple events at the same step into a single row to avoid duplicate x-axis
    # categories (which can cause apparent "jumps" for dense series when sparse series are interleaved).
    step_rows: Dict[int, Dict[str, Any]] = {}
    keys: set[str] = set()
    for evt in _iter_events(events_path):
        if not isinstance(evt, dict) or evt.get("type") != "metrics":
            continue
        data = evt.get("data") or {}
        if not isinstance(data, dict):
            continue
        k = "global_step" if "global_step" in data else ("step" if "step" in data else None)
        if k is None:
            continue
        try:
            step_val = int(data[k])
        except Exception:
            continue
        row = step_rows.get(step_val)
        if row is None:
            row = {"global_step": step_val}
            step_rows[step_val] = row
        for kk, vv in data.items():
            if kk in ("global_step", "step", "epoch"):
                continue
            if isinstance(vv, (int, float, str)) or vv is None:
                row[kk] = sanitize_value(vv)  # Sanitize NaN/Inf values
                keys.add(kk)
    if not step_rows:
        return [], []
    rows = [step_rows[s] for s in sorted(step_rows.keys())]
    cols = ["global_step"] + sorted(list(keys))
    for r in rows:
        for c in cols:
            r.setdefault(c, None)
    return cols, rows


# ---------------- GPU telemetry ----------------

def _which_nvidia_smi() -> Optional[str]:
    try:
        found = shutil.which("nvidia-smi")
        if found:
            return found
        if os.name == "nt":
            for p in [
                r"C:\\Windows\\System32\\nvidia-smi.exe",
                r"C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe",
            ]:
                if os.path.exists(p):
                    return p
        return None
    except Exception:
        return None


def _to_float(val: str) -> Optional[float]:
    try:
        x = val.strip()
        if not x or x.upper() == "N/A":
            return None
        return float(x)
    except Exception:
        return None


def _read_gpu_telemetry() -> dict:
    path = _which_nvidia_smi()
    if not path:
        return {"available": False, "reason": "nvidia-smi not found in PATH"}
    fields = [
        "index","name","utilization.gpu","utilization.memory","memory.total","memory.used",
        "temperature.gpu","power.draw","power.limit","clocks.sm","clocks.mem","pstate","fan.speed",
    ]
    cmd = [path, f"--query-gpu={','.join(fields)}", "--format=csv,noheader,nounits"]
    try:
        out = os.popen(" ".join(cmd)).read()
        lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
        gpus: List[dict] = []
        for ln in lines:
            parts = [p.strip() for p in ln.split(",")]
            if len(parts) != len(fields):
                if len(parts) > len(fields):
                    idx = parts[0]
                    name = ",".join(parts[1 : len(parts) - (len(fields) - 2)])
                    tail = parts[len(parts) - (len(fields) - 2) :]
                    parts = [idx, name] + tail
                else:
                    continue
            d = {
                "index": int(_to_float(parts[0]) or 0),
                "name": parts[1],
                "util_gpu": _to_float(parts[2]),
                "util_mem": _to_float(parts[3]),
                "mem_total_mib": _to_float(parts[4]),
                "mem_used_mib": _to_float(parts[5]),
                "temp_c": _to_float(parts[6]),
                "power_w": _to_float(parts[7]),
                "power_limit_w": _to_float(parts[8]),
                "clock_sm_mhz": _to_float(parts[9]),
                "clock_mem_mhz": _to_float(parts[10]),
                "pstate": parts[11],
                "fan_speed_pct": _to_float(parts[12]),
            }
            try:
                if d.get("mem_total_mib") and d.get("mem_used_mib") is not None:
                    d["mem_used_pct"] = max(0.0, min(100.0, (d["mem_used_mib"] or 0.0) * 100.0 / max(1.0, d["mem_total_mib"])) )
            except Exception:
                pass
            gpus.append(d)
        return {"available": True, "ts": _ts(), "gpus": gpus}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------- App factory ----------------

def create_app(storage: Optional[str] = None) -> FastAPI:
    root = _storage_root(storage)
    # Initialize logging
    _setup_logging()
    app = FastAPI(title="Runicorn Viewer", version="0.3.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*", "http://localhost:5173", "http://127.0.0.1:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Background task to check process status
    _status_check_task = None
    
    @app.on_event("startup")
    async def startup_event():
        """Start background status checking task."""
        nonlocal _status_check_task
        _status_check_task = asyncio.create_task(_periodic_status_check(root))
        logger.info("Started background process status checker")
    
    @app.on_event("shutdown") 
    async def shutdown_event():
        """Stop background status checking task."""
        if _status_check_task:
            _status_check_task.cancel()
            try:
                await _status_check_task
            except asyncio.CancelledError:
                pass
            logger.info("Stopped background process status checker")

    @app.get("/api/health")
    async def health():
        return {"status": "ok", "storage": str(root)}
    
    @app.post("/api/status/check")
    async def check_all_status():
        """Manually trigger status check for all running experiments."""
        checked_count = 0
        updated_count = 0
        
        for e in _iter_all_runs(root):
            d = e.dir
            status = _read_json(d / "status.json")
            if status.get("status") == "running":
                checked_count += 1
                # Store original status for comparison
                original_status = status.copy()
                _update_status_if_process_dead(d)
                # Re-read to see if it changed
                new_status = _read_json(d / "status.json")
                if new_status.get("status") != original_status.get("status"):
                    updated_count += 1
        
        return {
            "checked": checked_count,
            "updated": updated_count,
            "message": f"Checked {checked_count} running experiments, updated {updated_count} statuses"
        }
    
    @app.post("/api/runs/soft-delete")
    async def soft_delete_runs(payload: Dict[str, Any] = Body(...)):
        """Soft delete runs (move to recycle bin)."""
        run_ids = payload.get("run_ids", [])
        if not run_ids or not isinstance(run_ids, list):
            raise HTTPException(status_code=400, detail="run_ids is required and must be a list")
        
        results = {}
        for run_id in run_ids:
            entry = _find_run_dir_by_id(root, run_id)
            if not entry:
                results[run_id] = {"success": False, "error": "run not found"}
                continue
            
            # Check if already deleted
            if _is_run_deleted(entry.dir):
                results[run_id] = {"success": False, "error": "already deleted"}
                continue
            
            success = _soft_delete_run(entry.dir, "user_deleted")
            results[run_id] = {"success": success}
        
        successful_deletes = sum(1 for r in results.values() if r["success"])
        return {
            "deleted_count": successful_deletes,
            "results": results,
            "message": f"Soft deleted {successful_deletes} of {len(run_ids)} runs"
        }
    
    @app.get("/api/recycle-bin")
    async def list_deleted_runs():
        """List runs in recycle bin (soft deleted)."""
        items: List[Dict[str, Any]] = []
        for e in _iter_all_runs(root, include_deleted=True):
            if not _is_run_deleted(e.dir):
                continue  # Only show deleted runs
            
            d = e.dir
            rid = d.name
            meta = _read_json(d / "meta.json") 
            deleted_info = _read_json(d / ".deleted")
            
            proj = (meta.get("project") if isinstance(meta, dict) else None) or e.project
            name = (meta.get("name") if isinstance(meta, dict) else None) or e.name
            created = meta.get("created_at") if isinstance(meta, dict) else None
            if not isinstance(created, (int, float)):
                try:
                    created = d.stat().st_mtime
                except Exception:
                    created = None
            
            items.append({
                "id": rid,
                "project": proj,
                "name": name,
                "created_time": created,
                "deleted_at": deleted_info.get("deleted_at"),
                "delete_reason": deleted_info.get("reason", "unknown"),
                "original_status": deleted_info.get("original_status", "unknown"),
                "run_dir": str(d)
            })
        
        return {"deleted_runs": items}
    
    @app.post("/api/recycle-bin/restore")
    async def restore_runs(payload: Dict[str, Any] = Body(...)):
        """Restore runs from recycle bin."""
        run_ids = payload.get("run_ids", [])
        if not run_ids or not isinstance(run_ids, list):
            raise HTTPException(status_code=400, detail="run_ids is required and must be a list")
        
        results = {}
        for run_id in run_ids:
            entry = _find_run_dir_by_id(root, run_id, include_deleted=True)
            if not entry:
                results[run_id] = {"success": False, "error": "run not found"}
                continue
            
            if not _is_run_deleted(entry.dir):
                results[run_id] = {"success": False, "error": "run not deleted"}
                continue
            
            success = _restore_run(entry.dir)
            results[run_id] = {"success": success}
        
        successful_restores = sum(1 for r in results.values() if r["success"])
        return {
            "restored_count": successful_restores,
            "results": results,
            "message": f"Restored {successful_restores} of {len(run_ids)} runs"
        }
    
    @app.post("/api/recycle-bin/empty")
    async def empty_recycle_bin(payload: Dict[str, Any] = Body(...)):
        """Permanently delete all runs in recycle bin."""
        confirm = payload.get("confirm", False)
        if not confirm:
            raise HTTPException(status_code=400, detail="Must set confirm=true to permanently delete")
        
        deleted_count = 0
        for e in _iter_all_runs(root, include_deleted=True):
            if _is_run_deleted(e.dir):
                try:
                    import shutil
                    shutil.rmtree(e.dir)
                    deleted_count += 1
                    logger.info(f"Permanently deleted run: {e.dir.name}")
                except Exception as e:
                    logger.error(f"Failed to permanently delete {e.dir.name}: {e}")
        
        return {
            "permanently_deleted": deleted_count,
            "message": f"Permanently deleted {deleted_count} runs"
        }

    @app.get("/api/runs", response_model=List[RunListItem])
    async def list_runs():
        items: List[RunListItem] = []
        for e in _iter_all_runs(root):
            d = e.dir
            rid = d.name
            
            # Check and update process status if needed
            _update_status_if_process_dead(d)
            
            meta = _read_json(d / "meta.json")
            status = _read_json(d / "status.json")
            summ = _read_json(d / "summary.json")
            created = meta.get("created_at") if isinstance(meta, dict) else None
            if not isinstance(created, (int, float)):
                try:
                    created = d.stat().st_mtime
                except Exception:
                    created = None
            proj = (meta.get("project") if isinstance(meta, dict) else None) or e.project
            name = (meta.get("name") if isinstance(meta, dict) else None) or e.name
            # Get best metric info from summary
            best_metric_value = None
            best_metric_name = None
            if isinstance(summ, dict):
                best_metric_value = summ.get("best_metric_value")
                best_metric_name = summ.get("best_metric_name")
            
            items.append(
                RunListItem(
                    id=rid,
                    run_dir=str(d),
                    created_time=created,
                    status=str((status.get("status") if isinstance(status, dict) else "finished") or "finished"),
                    pid=(meta.get("pid") if isinstance(meta, dict) else None),
                    best_metric_value=best_metric_value,
                    best_metric_name=best_metric_name,
                    project=proj,
                    name=name,
                )
            )
        return items

    @app.get("/api/runs/{run_id}")
    async def run_detail(run_id: str):
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail="run not found")
        d = entry.dir
        
        # Check and update process status if needed
        _update_status_if_process_dead(d)
        
        meta = _read_json(d / "meta.json")
        status = _read_json(d / "status.json")
        proj = (meta.get("project") if isinstance(meta, dict) else None) or entry.project
        name = (meta.get("name") if isinstance(meta, dict) else None) or entry.name
        return {
            "id": run_id,
            "status": str((status.get("status") if isinstance(status, dict) else "finished") or "finished"),
            "pid": (meta.get("pid") if isinstance(meta, dict) else None),
            "run_dir": str(d),
            "project": proj,
            "name": name,
            "logs": str(d / "logs.txt"),
            "metrics": str(d / "events.jsonl"),
            "metrics_step": str(d / "events.jsonl"),
        }

    @app.get("/api/runs/{run_id}/metrics")
    async def get_metrics(run_id: str):
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail="run not found")
        events = entry.dir / "events.jsonl"
        # Return step/time metrics for compatibility; epoch view is deprecated
        cols, rows = _aggregate_step_metrics(events)
        return {"columns": cols, "rows": rows}

    @app.get("/api/runs/{run_id}/metrics_step")
    async def get_metrics_step(run_id: str):
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail="run not found")
        events = entry.dir / "events.jsonl"
        cols, rows = _aggregate_step_metrics(events)
        return {"columns": cols, "rows": rows}

    @app.get("/api/runs/{run_id}/progress")
    async def get_progress(run_id: str):
        # Read-only viewer has no in-memory progress
        # Could estimate from events, but keep simple for MVP
        return {"available": False, "status": "unknown"}

    @app.websocket("/api/runs/{run_id}/logs/ws")
    async def logs_ws(websocket: WebSocket, run_id: str):
        await websocket.accept()
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            await websocket.send_text("[error] run not found")
            await websocket.close()
            return
        d = entry.dir
        log_file = d / "logs.txt"
        if not log_file.exists():
            await websocket.send_text("[info] logs.txt not found yet")
            await websocket.close()
            return
        try:
            async with aiofiles.open(log_file, mode="r", encoding="utf-8", errors="ignore") as f:
                await f.seek(0, os.SEEK_END)
                while True:
                    line = await f.readline()
                    if line:
                        await websocket.send_text(line.rstrip("\n"))
                    else:
                        await asyncio.sleep(0.5)
        except WebSocketDisconnect:
            return
        except Exception as e:
            try:
                await websocket.send_text(f"[error] {e}")
            finally:
                await websocket.close()

    @app.get("/api/gpu/telemetry")
    async def gpu_telemetry():
        return _read_gpu_telemetry()

    # ---- Config management ----
    class SetUserRootBody(BaseModel):
        path: str

    @app.get("/api/config")
    async def get_config():
        return {
            "user_root_dir": str(get_user_root_dir() or ""),
            "storage": str(root),
        }

    @app.post("/api/config/user_root_dir")
    async def set_user_root(payload: Dict[str, Any] = Body(...)):
        nonlocal root
        try:
            # Accept plain dict to avoid model parsing edge-cases in frozen builds
            raw = payload.get("path") if isinstance(payload, dict) else None
            in_path = str(raw or "")
            logger.debug(f"set_user_root called with path='{in_path}'")
            # Expand env vars on all platforms (Windows: %VAR%, POSIX: $VAR)
            in_path = os.path.expandvars(in_path)
            p = set_user_root_dir(in_path)
        except Exception as e:
            logger.error(f"set_user_root_dir failed: {e}")
            raise HTTPException(status_code=400, detail=f"invalid path or permission: {e}")

        try:
            # Recompute storage root to apply immediately using the path we just set
            # Passing it explicitly avoids racing on config read and prevents CWD fallback
            root = _storage_root(str(p))
        except Exception as e:
            logger.error(f"_storage_root reinit failed: {e}")
            raise HTTPException(status_code=500, detail=f"failed to reinitialize storage root: {e}")

        return {
            "ok": True,
            "user_root_dir": str(p),
            "storage": str(root),
        }

    # ---- SSH remote browse & live mirror ----
    # Models are defined at module scope (see top of file) to avoid Pydantic forward-ref issues.

    @app.post("/api/ssh/connect")
    async def ssh_connect(payload: Dict[str, Any] = Body(...)):
        try:
            host = str(payload.get("host") or "").strip()
            username = str(payload.get("username") or "").strip()
            if not host or not username:
                raise HTTPException(status_code=400, detail="host and username are required")
            port = int(payload.get("port") or 22)
            sess = ssh_sync.create_session(
                host=host,
                port=port,
                username=username,
                password=payload.get("password"),
                pkey_str=payload.get("pkey"),
                pkey_path=payload.get("pkey_path"),
                passphrase=payload.get("passphrase"),
                use_agent=bool(payload.get("use_agent", True)),
            )
            return {"ok": True, "session_id": sess.id}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"ssh connect failed: {e}")

    @app.get("/api/ssh/sessions")
    async def ssh_sessions():
        return {"sessions": ssh_sync.list_sessions()}

    # (model at module level) SSHCloseBody

    @app.post("/api/ssh/close")
    async def ssh_close(payload: Dict[str, Any] = Body(...)):
        sid = str(payload.get("session_id") or "").strip()
        if not sid:
            raise HTTPException(status_code=400, detail="session_id required")
        ok = ssh_sync.close_session(sid)
        return {"ok": bool(ok)}

    @app.get("/api/ssh/listdir")
    async def ssh_listdir(session_id: str, path: Optional[str] = None):
        try:
            items = ssh_sync.sftp_listdir(session_id, path or "~")
            return {"items": items}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    # (model at module level) SSHMirrorStartBody

    @app.post("/api/ssh/mirror/start")
    async def ssh_mirror_start(payload: Dict[str, Any] = Body(...)):
        try:
            sid = str(payload.get("session_id") or "").strip()
            remote_root = str(payload.get("remote_root") or "").strip()
            if not sid or not remote_root:
                raise HTTPException(status_code=400, detail="session_id and remote_root are required")
            interval = float(payload.get("interval") or 2.0)
            task = ssh_sync.start_mirror(session_id=sid, remote_root=remote_root, local_root=root, interval=interval)
            return {"ok": True, "task": {
                "id": task.id,
                "session_id": task.session.id,
                "remote_root": task.remote_root,
                "local_root": str(task.local_root),
                "interval": task.interval,
                "stats": dict(task.stats),
            }}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"mirror start failed: {e}")

    # (model at module level) SSHMirrorStopBody

    @app.post("/api/ssh/mirror/stop")
    async def ssh_mirror_stop(payload: Dict[str, Any] = Body(...)):
        tid = str(payload.get("task_id") or "").strip()
        if not tid:
            raise HTTPException(status_code=400, detail="task_id required")
        ok = ssh_sync.stop_mirror(tid)
        return {"ok": bool(ok)}

    @app.get("/api/ssh/mirror/list")
    async def ssh_mirror_list():
        return {"mirrors": ssh_sync.list_mirrors(), "storage": str(root)}
    
    # ---- Experiment Management ----
    @app.post("/api/experiments/tag")
    async def tag_experiment(payload: Dict[str, Any] = Body(...)):
        """Add tags to an experiment."""
        if not HAS_EXPERIMENT_MANAGER:
            raise HTTPException(status_code=501, detail="Experiment management not available")
        
        run_id = payload.get("run_id")
        tags = payload.get("tags", [])
        append = payload.get("append", True)
        
        if not run_id:
            raise HTTPException(status_code=400, detail="run_id is required")
        
        try:
            manager = ExperimentManager(root)
            success = manager.tag_experiment(run_id, tags, append)
            return {"success": success}
        except Exception as e:
            logger.error(f"Failed to tag experiment: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/api/experiments/search")
    async def search_experiments(
        project: Optional[str] = None,
        tags: Optional[str] = None,  # Comma-separated
        text: Optional[str] = None,
        archived: bool = False
    ):
        """Search experiments by various criteria."""
        if not HAS_EXPERIMENT_MANAGER:
            raise HTTPException(status_code=501, detail="Experiment management not available")
        
        try:
            manager = ExperimentManager(root)
            tag_list = tags.split(",") if tags else None
            results = manager.search_experiments(
                project=project,
                tags=tag_list,
                text=text,
                archived=archived
            )
            return {"experiments": [r.to_dict() for r in results]}
        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.delete("/api/experiments/delete")
    async def delete_experiments(payload: Dict[str, Any] = Body(...)):
        """Delete experiments."""
        if not HAS_EXPERIMENT_MANAGER:
            raise HTTPException(status_code=501, detail="Experiment management not available")
        
        run_ids = payload.get("run_ids", [])
        force = payload.get("force", False)
        
        if not run_ids:
            raise HTTPException(status_code=400, detail="run_ids are required")
        
        try:
            manager = ExperimentManager(root)
            results = manager.delete_experiments(run_ids, force)
            return {"results": results}
        except Exception as e:
            logger.error(f"Delete failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    # ---- Data Export ----
    @app.get("/api/export/{run_id}/csv")
    async def export_csv(run_id: str):
        """Export run metrics as CSV."""
        if not HAS_EXPORTER:
            raise HTTPException(status_code=501, detail="Export functionality not available")
        
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail=f"Run {run_id} not found")
        
        try:
            exporter = MetricsExporter(entry.dir)
            csv_content = exporter.to_csv()
            
            if csv_content:
                from fastapi.responses import Response
                return Response(
                    content=csv_content,
                    media_type="text/csv",
                    headers={"Content-Disposition": f"attachment; filename={run_id}_metrics.csv"}
                )
            else:
                raise HTTPException(status_code=404, detail="No metrics to export")
        except Exception as e:
            logger.error(f"CSV export failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/api/export/{run_id}/report")
    async def export_report(run_id: str, format: str = "markdown"):
        """Generate experiment report."""
        if not HAS_EXPORTER:
            raise HTTPException(status_code=501, detail="Export functionality not available")
        
        if format not in ["markdown", "html"]:
            raise HTTPException(status_code=400, detail="Format must be markdown or html")
        
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail=f"Run {run_id} not found")
        
        try:
            exporter = MetricsExporter(entry.dir)
            import tempfile
            
            with tempfile.NamedTemporaryFile(mode='w', suffix=f'.{format}', delete=False) as f:
                temp_path = Path(f.name)
            
            if format == "markdown":
                success = exporter._generate_markdown_report(temp_path)
            else:
                success = exporter._generate_html_report(temp_path)
            
            if success and temp_path.exists():
                content = temp_path.read_text(encoding='utf-8')
                temp_path.unlink()  # Clean up temp file
                
                media_type = "text/markdown" if format == "markdown" else "text/html"
                from fastapi.responses import Response
                return Response(
                    content=content,
                    media_type=media_type,
                    headers={"Content-Disposition": f"attachment; filename={run_id}_report.{format}"}
                )
            else:
                raise HTTPException(status_code=500, detail="Report generation failed")
        except Exception as e:
            logger.error(f"Report generation failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/api/environment/{run_id}")
    async def get_environment(run_id: str):
        """Get environment information for a run."""
        entry = _find_run_dir_by_id(root, run_id)
        if not entry:
            raise HTTPException(status_code=404, detail=f"Run {run_id} not found")
        
        env_path = entry.dir / "environment.json"
        if not env_path.exists():
            return {"available": False}
        
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                env_data = json.load(f)
            return {"available": True, "environment": env_data}
        except Exception as e:
            logger.error(f"Failed to load environment: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    # ---- Offline import (zip/tar.gz) ----
    def _is_within_directory(base: Path, target: Path) -> bool:
        try:
            base_resolved = base.resolve()
            target_resolved = target.resolve()
            return str(target_resolved).startswith(str(base_resolved))
        except Exception:
            return False

    def _safe_extract_tar(tar: tarfile.TarFile, dest: Path) -> List[Path]:
        extracted: List[Path] = []
        for member in tar.getmembers():
            if not member.name or member.name.strip() == "":
                continue
            # Skip symlinks/hardlinks for safety
            try:
                if member.issym() or member.islnk():
                    continue
            except Exception:
                pass
            # Prevent path traversal
            target_path = dest / member.name
            if not _is_within_directory(dest, target_path):
                continue
            try:
                tar.extract(member, path=str(dest))
                if member.isdir():
                    continue
                extracted.append(target_path)
            except Exception:
                continue
        return extracted

    def _safe_extract_zip(zf: zipfile.ZipFile, dest: Path) -> List[Path]:
        extracted: List[Path] = []
        for name in zf.namelist():
            if not name or name.endswith("/"):
                # directories
                try:
                    (dest / name).mkdir(parents=True, exist_ok=True)
                except Exception:
                    pass
                continue
            target_path = dest / name
            if not _is_within_directory(dest, target_path):
                continue
            try:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(name) as src, open(target_path, "wb") as out:
                    out.write(src.read())
                extracted.append(target_path)
            except Exception:
                continue
        return extracted

    # Conditionally enable archive import (requires python-multipart)
    _mp_ok = True
    try:
        import multipart  # type: ignore
    except Exception:
        _mp_ok = False

    if _mp_ok:
        @app.post("/api/import/archive")
        async def import_archive(file: UploadFile = File(...)):
            """
            Import a packaged archive (.zip or .tar.gz/.tgz) of runs into the current storage root.

            Expected layout inside archive: either the storage root itself (project/name/runs/<id>)
            or any subset of that hierarchy. Files will be merged into the active storage root.
            """
            # Snapshot existing run dirs for delta reporting
            before = {e.dir for e in _iter_all_runs(root)}

            # Persist upload to a temp file first
            try:
                suffix = ".zip" if file.filename and file.filename.lower().endswith(".zip") else ".tar.gz"
            except Exception:
                suffix = ".zip"
            tmp = tempfile.NamedTemporaryFile(prefix="runicorn_import_", suffix=suffix, delete=False)
            tmp_path = Path(tmp.name)
            try:
                while True:
                    chunk = await file.read(1024 * 1024)
                    if not chunk:
                        break
                    tmp.write(chunk)
            finally:
                tmp.close()

            # Detect and extract
            imported_files: List[Path] = []
            try:
                fn = (file.filename or "").lower()
                if fn.endswith(".zip"):
                    with zipfile.ZipFile(tmp_path, "r") as zf:
                        imported_files = _safe_extract_zip(zf, root)
                elif fn.endswith(".tar.gz") or fn.endswith(".tgz"):
                    with tarfile.open(tmp_path, "r:gz") as tf:
                        imported_files = _safe_extract_tar(tf, root)
                else:
                    # Try zip first, then tar.gz
                    try:
                        with zipfile.ZipFile(tmp_path, "r") as zf:
                            imported_files = _safe_extract_zip(zf, root)
                    except Exception:
                        try:
                            with tarfile.open(tmp_path, "r:gz") as tf:
                                imported_files = _safe_extract_tar(tf, root)
                        except Exception as e2:
                            raise HTTPException(status_code=400, detail=f"unsupported or corrupted archive: {e2}")
            finally:
                try:
                    tmp_path.unlink(missing_ok=True)
                except Exception:
                    pass

            # Compute imported runs delta
            after_entries = _iter_all_runs(root)
            after = {e.dir for e in after_entries}
            new_dirs = sorted([str(p) for p in (after - before)])
            # Map run_ids for quick display
            new_ids: List[str] = []
            for e in after_entries:
                if e.dir in (after - before):
                    new_ids.append(e.dir.name)

            return {
                "ok": True,
                "imported_files": len(imported_files),
                "new_run_dirs": new_dirs,
                "new_run_ids": sorted(new_ids),
                "storage": str(root),
            }
    else:
        @app.post("/api/import/archive")
        async def import_archive_unavailable():
            # Provide a stub to avoid breaking UI calls; returns Service Unavailable
            raise HTTPException(status_code=503, detail="File upload not available: python-multipart not bundled in this build")

    # ---- Project/Name discovery APIs ----
    @app.get("/api/projects")
    async def list_projects():
        projs: set[str] = set()
        for e in _iter_all_runs(root):
            if e.project:
                projs.add(e.project)
            else:
                # legacy runs: try meta
                meta = _read_json(e.dir / "meta.json")
                p = meta.get("project") if isinstance(meta, dict) else None
                if p:
                    projs.add(str(p))
        return {"projects": sorted(projs)}

    @app.get("/api/projects/{project}/names")
    async def list_names(project: str):
        names: set[str] = set()
        for e in _iter_all_runs(root):
            # prefer explicit fields
            p = e.project
            n = e.name
            if not p or p != project:
                # try meta
                meta = _read_json(e.dir / "meta.json")
                p2 = meta.get("project") if isinstance(meta, dict) else None
                n2 = meta.get("name") if isinstance(meta, dict) else None
                if p2 == project and n2:
                    names.add(str(n2))
                continue
            if n:
                names.add(n)
        return {"names": sorted(names)}

    @app.get("/api/projects/{project}/names/{name}/runs", response_model=List[RunListItem])
    async def list_runs_by_name(project: str, name: str):
        items: List[RunListItem] = []
        for e in _iter_all_runs(root):
            meta = _read_json(e.dir / "meta.json")
            p = (meta.get("project") if isinstance(meta, dict) else None) or e.project
            n = (meta.get("name") if isinstance(meta, dict) else None) or e.name
            if p != project or n != name:
                continue
            d = e.dir
            rid = d.name
            
            # Check and update process status if needed
            _update_status_if_process_dead(d)
            
            status = _read_json(d / "status.json")
            summ = _read_json(d / "summary.json")
            created = meta.get("created_at") if isinstance(meta, dict) else None
            if not isinstance(created, (int, float)):
                try:
                    created = d.stat().st_mtime
                except Exception:
                    created = None
            # Get best metric info from summary
            best_metric_value = None
            best_metric_name = None
            if isinstance(summ, dict):
                best_metric_value = summ.get("best_metric_value")
                best_metric_name = summ.get("best_metric_name")
            
            items.append(
                RunListItem(
                    id=rid,
                    run_dir=str(d),
                    created_time=created,
                    status=str((status.get("status") if isinstance(status, dict) else "finished") or "finished"),
                    pid=(meta.get("pid") if isinstance(meta, dict) else None),
                    best_metric_value=best_metric_value,
                    best_metric_name=best_metric_name,
                    project=p,
                    name=n,
                )
            )
        return items

    # ---- Static frontend mounting ----
    # Prefer an explicit frontend dist path provided via env var for dev/desktop
    try:
        env_dir_s = os.environ.get("RUNICORN_FRONTEND_DIST") or os.environ.get("RUNICORN_DESKTOP_FRONTEND")
        if env_dir_s:
            env_dir = Path(env_dir_s)
            if env_dir.exists():
                # Mount at root; '/api' routes remain available since they are explicit
                app.mount("/", StaticFiles(directory=str(env_dir), html=True), name="frontend")
                return app
    except Exception:
        pass
    # Fallback: serve the packaged webui if present inside the Python package
    try:
        ui_dir = Path(__file__).parent / "webui"
        if ui_dir.exists():
            app.mount("/", StaticFiles(directory=str(ui_dir), html=True), name="frontend")
    except Exception:
        # Static UI not found or failed to mount; API still works (dev can use external server)
        pass

    return app
