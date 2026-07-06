from pydantic import BaseModel
from enum import Enum

class StatusTypes(str, Enum):
    healthy = "healthy"
    unhealthy = "unhealthy"


class HealthCheckResponse(BaseModel):
    status: StatusTypes
    timestamp: str