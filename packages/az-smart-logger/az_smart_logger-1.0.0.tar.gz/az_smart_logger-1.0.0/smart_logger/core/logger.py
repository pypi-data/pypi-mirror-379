# smart_logger/core/smart_logger.py
"""
Production-ready SmartLogger.

Place this file at smart_logger/core/smart_logger.py
Requires:
 - smart_logger.core.base_config: LOG_DIR, DEFAULT_LOG_LEVEL
 - .file_manager: FileManager with get_log_file(base_dir, parent_folder, filename)
 - .db_handler: DBHandler with insert_log_metadata(...) or insert_batch_metadata(list_of_dicts)
 - .utils: generate_uuid()

Behavior:
 - Main logs: LOG_DIR/YYYY-MM-DD/<parent_folder>/<filename>
 - Temp log: smart_logger/_temp.log (single file)
 - Use SmartLogger("app.log") and then logger.info(...), logger.error(...), ...
 - Must call logger.shutdown() at graceful exit OR the atexit hook will try to flush.
"""

from __future__ import annotations
import atexit
import inspect
import traceback
from datetime import datetime
from pathlib import Path
from queue import Queue, Full, Empty
from threading import Thread, Lock, Event
from typing import Optional, List, Dict, Any
import time
from smart_logger.core.base_config import DEFAULT_LOG_LEVEL, LOG_DIR
from .file_manager import FileManager
from .db_handler import DBHandler
from .utils import generate_uuid

# Temp file in smart_logger/ root
TEMP_FILE_NAME = "_temp.log"
SMART_LOGGER_ROOT = Path(__file__).resolve().parent.parent

# Internal fallback error file if worker faces exceptions
WORKER_ERR_FILE = SMART_LOGGER_ROOT / "_worker_errors.log"

# Defaults tuned for high-throughput production — you can change during init
DEFAULT_QUEUE_MAXSIZE = 20000          # bounded queue to apply backpressure
DEFAULT_BATCH_SIZE = 10               # number of log entries to write per disk/db batch
DEFAULT_BATCH_WAIT = 0.05              # max seconds to wait to build a batch
PUT_TIMEOUT = 0.5                       # seconds to block when putting to queue before raising Full

# If True and queue is full, drop the log instead of blocking/raising (helps availability)
DEFAULT_DROP_ON_FULL = False


# -----------------------
# Worker Thread
# -----------------------
class LoggerWorker(Thread):
    """
    Background worker that collects log items from a Queue, writes them in batches to
    appropriate log files + temp log, and stores metadata to DB in batch.
    """

    def __init__(
        self,
        queue: Queue,
        file_manager: FileManager,
        db_handler: DBHandler,
        batch_size: int = DEFAULT_BATCH_SIZE,
        batch_wait: float = DEFAULT_BATCH_WAIT
    ):
        super().__init__(daemon=False)  # non-daemon; we will shutdown explicitly
        self.queue = queue
        self.file_manager = file_manager
        self.db_handler = db_handler
        self.batch_size = max(1, batch_size)
        self.batch_wait = max(0.0, batch_wait)
        self.stop_event = Event()
        self.lock = Lock()
        self.temp_file = SMART_LOGGER_ROOT / TEMP_FILE_NAME

        # ensure temp file directory exists (smart_logger/)
        self.temp_file.parent.mkdir(parents=True, exist_ok=True)

    def run(self):
        """
        Continuously collect items and process them in batches until stop requested.
        """
        try:
            while not self.stop_event.is_set():
                batch = []
                start_time = time.time()
                # Block until at least one item is available or stop
                try:
                    item = self.queue.get(timeout=0.2)
                except Empty:
                    continue

                if item is None:
                    # Shutdown sentinel
                    self.queue.task_done()
                    break

                batch.append(item)
                # collect until batch_size or batch_wait exceeded
                while len(batch) < self.batch_size and (time.time() - start_time) < self.batch_wait:
                    try:
                        item = self.queue.get(timeout=self.batch_wait)
                    except Empty:
                        break
                    if item is None:
                        self.queue.task_done()
                        self.stop_event.set()
                        break
                    batch.append(item)

                # process batch
                try:
                    self._process_batch(batch)
                except Exception:
                    # If something goes wrong while processing, log stacktrace to worker error file
                    with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                        ef.write(f"[{datetime.utcnow().isoformat()}] Worker exception:\n")
                        ef.write(traceback.format_exc())
                        ef.write("\n---\n")
                finally:
                    for _ in batch:
                        try:
                            self.queue.task_done()
                        except Exception:
                            pass

            # Process remaining items if any before exit
            remaining = []
            while True:
                try:
                    item = self.queue.get_nowait()
                    if item is None:
                        self.queue.task_done()
                        break
                    remaining.append(item)
                    self.queue.task_done()
                except Empty:
                    break

            if remaining:
                try:
                    self._process_batch(remaining)
                except Exception:
                    with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                        ef.write(f"[{datetime.utcnow().isoformat()}] Worker exception on final drain:\n")
                        ef.write(traceback.format_exc())
                        ef.write("\n---\n")

        except Exception:
            with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                ef.write(f"[{datetime.utcnow().isoformat()}] Unhandled worker exception:\n")
                ef.write(traceback.format_exc())
                ef.write("\n---\n")

    def stop(self):
        self.stop_event.set()

    def _format_line(self, data: Dict[str, Any]) -> str:
        # Use ISO timestamp for readability
        ts = data.get("timestamp")
        if hasattr(ts, "isoformat"):
            ts_str = ts.isoformat()
        else:
            ts_str = str(ts)
        base = f"[{data['uuid']}] [{data['log_type']}] {ts_str} {data['module']}.{data['funcName']}:{data['line']} | {data['message']}"
        if data.get("ip_address"):
            base += f" [IP: {data['ip_address']}]"
        return base + "\n"

    def _process_batch(self, batch: List[Dict[str, Any]]):
        """
        Write all batch entries to their respective main log files (using FileManager),
        append all to the single temp file, and insert metadata to DB in batch if supported.
        """
        # group by log_file_path to minimize open/close
        writes: Dict[Path, List[str]] = {}
        temp_lines: List[str] = []
        db_rows: List[Dict[str, Any]] = []

        for data in batch:
            try:
                log_file_path = self.file_manager.get_log_file(data["parent_folder"], data["filename"])
                line = self._format_line(data)
                writes.setdefault(log_file_path, []).append(line)
                temp_lines.append(line)

                db_rows.append({
                    "uuid": data["uuid"],
                    "datetime": data["timestamp"],
                    "parent_folder": data["parent_folder"],  
                    "filename": data["filename"],
                    "full_path": str(log_file_path),
                    "log_type": data["log_type"],
                    "ip_address": data.get("ip_address") or "0.0.0.0", 
                    "module": data["module"],
                })
            except Exception:
                # If building one entry fails, write error to worker file but continue
                with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                    ef.write(f"[{datetime.utcnow().isoformat()}] Failed preparing log_data: {traceback.format_exc()}\n")

        # Write to respective files
        with self.lock:
            for path, lines in writes.items():
                try:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with open(path, "a", encoding="utf-8") as f:
                        f.writelines(lines)
                except Exception:
                    with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                        ef.write(f"[{datetime.utcnow().isoformat()}] Failed writing to {path}: {traceback.format_exc()}\n")

            # Append all to temp log
            if temp_lines and self.db_handler.get_active_clients():
                try:
                    with open(self.temp_file, "a", encoding="utf-8") as tf:
                        tf.writelines(temp_lines)
                except Exception:
                    with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                        ef.write(f"[{datetime.utcnow().isoformat()}] Failed writing to temp file: {traceback.format_exc()}\n")

        # Insert metadata into DB (try batch first)
        try:
            if hasattr(self.db_handler, "insert_batch_metadata"):
                self.db_handler.insert_batch_metadata(db_rows)
            else:
                # fallback to single inserts
                for row in db_rows:
                    try:
                        self.db_handler.insert_log_metadata(**row)
                    except Exception:
                        with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                            ef.write(f"[{datetime.utcnow().isoformat()}] DB insert failed: {traceback.format_exc()}\n")
        except Exception:
            with open(WORKER_ERR_FILE, "a", encoding="utf-8") as ef:
                ef.write(f"[{datetime.utcnow().isoformat()}] DB batch insert failed: {traceback.format_exc()}\n")


# -----------------------
# SmartLogger (public)
# -----------------------
class SmartLogger:
    """
    Public API:
      logger = SmartLogger(filename="app.log", base_dir=LOG_DIR, ...)
      logger.info("msg")
      logger.error("msg")
      logger.shutdown()
      reader = TempLogReader()
      line = reader.get_line()
    """

    _instance: Optional["SmartLogger"] = None

    def __new__(cls, *args, **kwargs):
        # Singleton across process
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        base_dir: Path = LOG_DIR,
        log_level: str = DEFAULT_LOG_LEVEL,
        queue_maxsize: int = DEFAULT_QUEUE_MAXSIZE,
        batch_size: int = DEFAULT_BATCH_SIZE,
        batch_wait: float = DEFAULT_BATCH_WAIT,
        drop_on_full: bool = DEFAULT_DROP_ON_FULL,
    ):
        if getattr(self, "_initialized", False):
            return

        self.file_manager = FileManager(base_dir)
        self.db_handler = DBHandler()
        self.log_level = log_level
        self.drop_on_full = bool(drop_on_full)

        # bounded queue for backpressure
        self._queue: Queue = Queue(maxsize=max(0, int(queue_maxsize)))
        self._worker = LoggerWorker(self._queue, self.file_manager, self.db_handler, batch_size=batch_size, batch_wait=batch_wait)
        # start worker
        self._worker.start()

        # register safe shutdown at process exit
        atexit.register(self.shutdown)

        self._initialized = True

    # Internal helper to push to queue with backpressure policy
    def _enqueue(self, payload: Dict[str, Any]) -> bool:
        try:
            self._queue.put(payload, timeout=PUT_TIMEOUT)
            return True
        except Full:
            if self.drop_on_full:
                # optional: might record a dropped counter to metrics
                return False
            else:
                # As fallback, attempt a non-blocking put and drop if still full
                try:
                    self._queue.put_nowait(payload)
                    return True
                except Full:
                    return False

    def _log(self, message: str, log_type: str = "INFO", ip_address: Optional[str] = None) -> bool:
        """
        Prepare the payload and enqueue it. Returns True if enqueued successfully.
        """
        uuid_str = generate_uuid()
        timestamp = datetime.utcnow()

        caller = inspect.stack()[2]
        caller_path = Path(caller.filename)

        # Module name without extension
        module = caller_path.stem          # e.g., "views" from "views.py"
        # Parent folder name
        parent_folder = caller_path.parent.name # e.g., "blog" if path is "/project/blog/views.py"
        # Log filename
        filename = f"{module}.log" 

        payload = {
            "uuid": uuid_str,
            "timestamp": timestamp,
            "parent_folder": parent_folder,
            "filename": filename,
            "log_type": log_type.upper(),
            "module": module,
            "funcName": caller.function,
            "line": caller.lineno,
            "message": message,
            "ip_address": ip_address or None,
        }

        return self._enqueue(payload)

    # Public logging methods; return bool whether accepted
    def debug(self, message: str, ip_address: Optional[str] = None) -> bool:
        return self._log(message, "DEBUG", ip_address)

    def info(self, message: str, ip_address: Optional[str] = None) -> bool:
        return self._log(message, "INFO", ip_address)

    def warning(self, message: str, ip_address: Optional[str] = None) -> bool:
        return self._log(message, "WARNING", ip_address)

    def error(self, message: str, ip_address: Optional[str] = None) -> bool:
        return self._log(message, "ERROR", ip_address)

    def critical(self, message: str, ip_address: Optional[str] = None) -> bool:
        return self._log(message, "CRITICAL", ip_address)

    # Temp file reading for frontend (last N lines)
    def read_temp_logs(self, max_lines: int = 50) -> List[str]:
        temp_file = SMART_LOGGER_ROOT / TEMP_FILE_NAME
        if not temp_file.exists():
            return []
        with Lock():
            with open(temp_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            return [l.rstrip("\n") for l in lines[-max_lines:]]

    # Remove specific lines (after sending)
    def remove_sent_logs(self, lines_to_remove: List[str]):
        temp_file = SMART_LOGGER_ROOT / TEMP_FILE_NAME
        if not temp_file.exists():
            return
        with Lock():
            with open(temp_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            remaining = [l for l in lines if l.rstrip("\n") not in set(lines_to_remove)]
            with open(temp_file, "w", encoding="utf-8") as f:
                f.writelines(remaining)

    # Shutdown function to flush & stop worker cleanly
    def shutdown(self, timeout: float = 10.0):
        """
        Flushes queue and stops worker. Should be called at graceful shutdown.
        A registered atexit handler will call this automatically if you forget.
        """
        # Enqueue sentinel None to indicate shutdown
        try:
            # put None even if queue full (block a bit)
            self._queue.put(None, timeout=2.0)
        except Exception:
            # If we can't enqueue sentinel, set stop and hope worker drains quickly
            self._worker.stop()

        # Wait for worker to finish
        self._worker.join(timeout=timeout)

    # TempLogReader factory helper
    def get_temp_reader(self) -> "TempLogReader":
        return TempLogReader(SMART_LOGGER_ROOT / TEMP_FILE_NAME)


# -----------------------
# TempLogReader
# -----------------------
class TempLogReader:
    """
    Read a single line from the temp file and remove it atomically.
    Use this in a loop to stream lines to frontend and have them removed immediately.
    """

    def __init__(self, temp_file: Path = SMART_LOGGER_ROOT / TEMP_FILE_NAME):
        self.temp_file = temp_file
        self.lock = Lock()

    def get_line(self) -> Optional[str]:
        if not self.temp_file.exists():
            return None
        with self.lock:
            with open(self.temp_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            if not lines:
                return None
            line = lines[0]
            remaining = lines[1:]
            with open(self.temp_file, "w", encoding="utf-8") as f:
                f.writelines(remaining)
        return line.rstrip("\n")

