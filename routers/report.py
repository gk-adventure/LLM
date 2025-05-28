from fastapi import APIRouter, HTTPException
from schemas.report_schema import ReportRequest
from services.report_service import analyze_consumption

router = APIRouter()

@router.post("/reports")
def report_with_llm(request: ReportRequest):
    try:
        result = analyze_consumption(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))