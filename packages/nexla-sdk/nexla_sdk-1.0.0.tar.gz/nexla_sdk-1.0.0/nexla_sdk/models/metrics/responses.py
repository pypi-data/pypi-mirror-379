from typing import List, Optional, Dict, Any
from nexla_sdk.models.base import BaseModel


class AccountMetrics(BaseModel):
    """Account utilization metrics."""
    status: int
    metrics: List[Dict[str, Any]]


class DashboardMetricSet(BaseModel):
    """Dashboard metric set for a resource."""
    records: int
    size: int
    errors: int
    status: str  # OK, WARNING, ERROR


class DashboardMetrics(BaseModel):
    """24-hour dashboard metrics."""
    status: int
    metrics: Dict[str, Any]


class ResourceMetricDaily(BaseModel):
    """Daily resource metrics."""
    time: str  # Date in YYYY-MM-DD format
    records: int
    size: int
    errors: int


class ResourceMetricsByRun(BaseModel):
    """Resource metrics grouped by run."""
    runId: Optional[int] = None
    lastWritten: Optional[int] = None
    dataSetId: int
    records: int
    size: int
    errors: int


class MetricsResponse(BaseModel):
    """Generic metrics response."""
    status: int
    metrics: List[Any]  # Can be different types


class MetricsByRunResponse(BaseModel):
    """Metrics by run response with pagination."""
    status: int
    metrics: Dict[str, Any]  # Contains data and meta
