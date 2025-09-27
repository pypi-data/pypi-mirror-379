import datetime
from smart_logger.core.base_config import LOG_DIR
from sqlalchemy.orm import Session
from smart_logger.models.log_metadata import LogMetadata
import psutil
from fastapi.responses import FileResponse
from pathlib import Path
from typing import List, Optional
import zipfile
import io
from datetime import datetime
from smart_logger.core.db_handler import DBHandler
from smart_logger.models.log_metadata import LogMetadata
from sqlalchemy import func

BASE_LOG_DIR = Path(LOG_DIR)

class LogRepository:
    """Pure DB queries for LogMetadata."""

    @staticmethod
    def get_latest_logs(session: Session, limit: int = 50):
        return (
            session.query(LogMetadata)
            .order_by(LogMetadata.datetime.desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def count_all(session: Session) -> int:
        return session.query(LogMetadata).count()

    @staticmethod
    def count_by_level(session: Session, level: str) -> int:
        return session.query(LogMetadata).filter_by(log_type=level).count()


class LogServiceDetails:
    """Business logic for logs + stats."""

    @staticmethod
    def get_logs(session: Session, limit: int = 50):
        logs = LogRepository.get_latest_logs(session, limit)
        return [
            {
                "timestamp": log.datetime.strftime("%Y-%m-%d %H:%M:%S"),
                "level": log.log_type,
                "message": f"[{log.uuid}] {log.parent_folder}/{log.filename} | {log.module or ''}"
            }
            for log in logs
        ]

    @staticmethod
    def get_stats(session: Session):
        return {
            "total_logs": LogRepository.count_all(session),
            "info": LogRepository.count_by_level(session, "INFO"),
            "warnings": LogRepository.count_by_level(session, "WARNING"),
            "errors": LogRepository.count_by_level(session, "ERROR"),
            "critical": LogRepository.count_by_level(session, "CRITICAL"),
        }

    @staticmethod
    def get_system_info():
        # TODO: Replace with psutil or monitoring lib
        import datetime
        return {
            "cpu": f"{psutil.cpu_percent()}%",
            "memory": f"{psutil.virtual_memory().percent}%",
            "disk": f"{psutil.disk_usage('/').percent}%",
            "uptime": str(datetime.timedelta(seconds=int(psutil.boot_time())))
        }
 

class LogService:
    @staticmethod
    def parse_log_line(line: str):
        try:
            parts = line.split(" ")
            uuid = parts[0].strip("[]")
            log_type = parts[1].strip("[]")
            timestamp = datetime.strptime(f"{parts[2].split(".")[0].replace("T", " ")}", "%Y-%m-%d %H:%M:%S")
            message = " ".join(parts[7:])
            return {"uuid": uuid, "log_type": log_type, "timestamp": timestamp, "message": message, "raw": line.strip()}
        except Exception as be:
            print('oooooo', be)
            return None

    @classmethod
    def get_files_by_date(cls, date: str):
        folder_path = BASE_LOG_DIR / date
        if not folder_path.exists():
            return []
        files = []
        for f in folder_path.glob("**/*.log"):
            # Relative path from date folder
            rel_path = f.relative_to(folder_path)
            files.append(str(rel_path))  # e.g., "blog/view.log"
        return files

    @classmethod
    def get_logs_by_files(cls, date: str, files: List[str], start_time: str, end_time: str, uuid: Optional[str] = None):
        start_dt = datetime.strptime(f"{date} {start_time}:00", "%Y-%m-%d %H:%M:%S")
        end_dt   = datetime.strptime(f"{date} {end_time}:00", "%Y-%m-%d %H:%M:%S")
       
        logs = {}

        if not files:
            files = LogService.get_files_by_date(date)

        for file in files:
            file_path = BASE_LOG_DIR / date / file
            if not file_path.exists():
                continue
            logs[file] = []
            with open(file_path) as f:
                for line in f:
                    parsed = cls.parse_log_line(line)
                    if not parsed:
                        continue
                    if uuid and parsed["uuid"] != uuid:
                        continue
                    if start_dt <= parsed["timestamp"] <= end_dt:
                        logs[file].append(parsed["raw"])
        return logs

    @classmethod
    def get_logs_by_type(cls, date: str, log_type: str, start_time: str, end_time: str, uuid: Optional[str] = None):
        start_dt = datetime.strptime(start_time, "%H:%M:%S")
        end_dt = datetime.strptime(end_time, "%H:%M:%S")
        logs = []

        folder_path = BASE_LOG_DIR / date
        if not folder_path.exists():
            return []

        for file_path in folder_path.glob("**/*.log"):
            with open(file_path) as f:
                for line in f:
                    parsed = cls.parse_log_line(line)
                    if not parsed:
                        continue
                    if parsed["log_type"] != log_type:
                        continue
                    if uuid and parsed["uuid"] != uuid:
                        continue
                    if start_dt.time() <= parsed["timestamp"].time() <= end_dt.time():
                        logs.append(parsed["raw"])
        return logs

    @classmethod
    def download_logs_as_zip(cls, date: str, files: List[str]):
        date_path = BASE_LOG_DIR / date
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for file in files:
                file_path = date_path / file
                if file_path.exists():
                    zip_file.write(file_path, arcname=file)
        zip_buffer.seek(0)
        return FileResponse(zip_buffer, media_type="application/zip", filename=f"logs_{date}.zip")


class ChartsService:
    db = DBHandler()

    @classmethod
    def get_daywise_by_type(cls, date: str):
        """
        Day-wise error type counts
        date format: YYYY-MM-DD
        """
        session = cls.db.SessionLocal()
        try:
            results = session.query(
                LogMetadata.log_type,
                func.count(LogMetadata.uuid)
            ).filter(
                func.date(LogMetadata.datetime) == date
            ).group_by(LogMetadata.log_type).all()

            return {log_type: count for log_type, count in results}
        finally:
            session.close()

    @classmethod
    def get_monthwise(cls, month: str):
        """
        Month-wise logs count (per day)
        month format: YYYY-MM
        """
        session = cls.db.SessionLocal()
        try:
            results = session.query(
                func.to_char(LogMetadata.datetime, 'YYYY-MM-DD').label("day"),
                func.count(LogMetadata.uuid)
            ).filter(
                func.to_char(LogMetadata.datetime, 'YYYY-MM') == month
            ).group_by("day").order_by("day").all()

            return {day: count for day, count in results}
        finally:
            session.close()

    @classmethod
    def get_yearwise(cls, year: int):
        """
        Year-wise logs count (per month)
        year: int YYYY
        """
        session = cls.db.SessionLocal()
        try:
            results = session.query(
                func.to_char(LogMetadata.datetime, 'MM').label("month"),
                func.count(LogMetadata.uuid)
            ).filter(
                func.to_char(LogMetadata.datetime, 'YYYY') == str(year)
            ).group_by("month").order_by("month").all()

            return {month: count for month, count in results}
        finally:
            session.close()
