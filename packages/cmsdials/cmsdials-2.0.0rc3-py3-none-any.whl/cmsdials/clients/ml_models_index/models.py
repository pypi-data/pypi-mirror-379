from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ...utils.base_model import PaginatedBaseFilters, PaginatedBaseModel


class MLModelsIndex(BaseModel):
    id: int
    name: str
    revision: int
    ready: bool
    active: bool
    type: str
    anomaly_threshold: Optional[float]
    builtin_threshold: bool
    description: str
    flagging_key: Optional[str]
    input_signature: list[dict]
    metric_key: Optional[str]
    output_signature: list[dict]
    tags: Optional[list[dict]]
    isvc_service_name: Optional[str]
    isvc_yaml: Optional[str]
    created_by: str
    modified_by: str
    created_at: datetime
    modified_at: datetime


class PaginatedMLModelsIndexList(PaginatedBaseModel[MLModelsIndex]):
    pass


class MLModelsIndexFilters(PaginatedBaseFilters):
    id: Optional[int] = None
    id__in: Optional[list[int]] = None
    name: Optional[str] = None
    name__regex: Optional[str] = None
    active: Optional[bool] = None
    ready: Optional[bool] = None
    type: Optional[str] = None
    input_signature_contains_me: Optional[str] = None
    input_signature_contains_me__regex: Optional[str] = None
    tag_name: Optional[str] = None
    tag_value: Optional[str] = None
