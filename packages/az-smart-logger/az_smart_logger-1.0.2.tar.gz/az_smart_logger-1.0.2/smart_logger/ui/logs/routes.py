from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from smart_logger.core.db_handler import DBHandler
from smart_logger.ui.logs.services.logs_service import ChartsService, LogService, LogServiceDetails
from ..server import templates
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/logs", tags=["logs"])
db_handler = DBHandler()

# ---------------- HTML endpoints (same as before) ----------------
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    session: Session = db_handler.SessionLocal()
    try:
        logs = LogServiceDetails.get_logs(session, limit=50)
        stats = LogServiceDetails.get_stats(session)
        system = LogServiceDetails.get_system_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "logs": logs,
        "stats": stats,
        "system": system
    })


@router.get("/login-page", response_class=HTMLResponse)
async def login(request: Request):
    try:
        return templates.TemplateResponse("login.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/live-logs", response_class=HTMLResponse)
async def live_logs(request: Request):
    try:
        return templates.TemplateResponse("live_logs.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/filter_logs", response_class=HTMLResponse)
async def filter_logs_page(request: Request):
    try:
        return templates.TemplateResponse("filter_logs.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- JSON endpoints ----------------
@router.get("/files")
def get_files(date: str = Query(...)):
    try:
        files = LogService.get_files_by_date(date)
        return JSONResponse({"date": date, "files": files})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/logs_by_files")
def get_logs_by_files(
    date: Optional[str] = Query(None),
    files: Optional[List[str]] = Query(None),
    start_time: Optional[str] = Query(None),
    end_time: Optional[str] = Query(None),
    uuid: Optional[str] = Query(None)
):
    try:
        if not uuid:
            if not date or not files or not start_time or not end_time:
                return JSONResponse(
                    {"error": "All fields are mandatory if UUID is not provided"}, 
                    status_code=400
                )
        logs = LogService.get_logs_by_files(date, files, start_time, end_time, uuid)
        return JSONResponse({"date": date, "logs": logs})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/logs_by_type")
def get_logs_by_type(
    date: Optional[str] = Query(None),
    log_type: Optional[str] = Query(None),
    start_time: Optional[str] = Query(None),
    end_time: Optional[str] = Query(None),
    uuid: Optional[str] = Query(None)
):
    try:
        if not uuid:
            if not date or not log_type or not start_time or not end_time:
                return JSONResponse(
                    {"error": "All fields are mandatory if UUID is not provided"}, 
                    status_code=400
                )
        logs = LogService.get_logs_by_type(date, log_type, start_time, end_time, uuid)
        return JSONResponse({"date": date, "logs": logs})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/download_logs")
def download_logs(date: str = Query(...), files: List[str] = Query(...)):
    try:
        zip_path = LogService.download_logs_as_zip(date, files)
        return JSONResponse({"date": date, "files": files, "zip_path": zip_path})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/daywise_by_type")
def daywise_by_type(date: str = Query(...)):
    try:
        result = ChartsService.get_daywise_by_type(date=date)
        return {"date": date, "logs": result}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@router.get("/monthwise")
def monthwise(month: str = Query(...)):
    try:
        result = ChartsService.get_monthwise(month=month)
        return {"month": month, "logs": result}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@router.get("/yearwise")
def yearwise(year: str = Query(...)):
    try:
        result = ChartsService.get_yearwise(year=year)
        return {"year": year, "logs": result}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)