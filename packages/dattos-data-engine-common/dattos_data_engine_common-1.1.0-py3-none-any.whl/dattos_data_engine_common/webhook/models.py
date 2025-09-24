from typing import Optional
from pydantic import BaseModel

from dattos_data_engine_common.storage.models import StorageConfig


class BaseAsyncRequest(BaseModel):
    request_id: str
    heartbeat_check_seconds_interval: Optional[int] = None
    webhook_uri: Optional[str] = None
    webhook_token: Optional[str] = None
    storage: StorageConfig
