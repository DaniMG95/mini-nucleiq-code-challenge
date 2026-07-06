from fastapi import APIRouter, Request
from app.schemas.health import HealthCheckResponse, StatusTypes
from datetime import UTC, datetime


api_router = APIRouter(prefix="/health", tags=["health"])
@api_router.get("/", response_model=HealthCheckResponse)
async def health_check(request: Request):
    return HealthCheckResponse(status=StatusTypes.healthy, timestamp=datetime.now(UTC).isoformat())


