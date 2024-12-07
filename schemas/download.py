from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from utils.main import format_date

class BaseTimestamp(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")

    @classmethod
    def from_orm(cls, obj):
        return cls(
            createdAt=format_date(obj.created_at),
            updatedAt=format_date(obj.updated_at),
            deletedAt=format_date(obj.deleted_at)
        )

class DownloadCreate(BaseModel):
    url: str
    successful: bool
    media_type: Optional[str] = 'audio'
    created_at: Optional[str] = None
    
class DownloadResponse(BaseTimestamp):
    id: int
    url: str
    successful: bool
    media_type: str
    
    class Config:
        from_attributes = True