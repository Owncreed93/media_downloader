from collections import OrderedDict
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from utils.main import format_date

class BaseTimestamp(BaseModel):
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)

    @classmethod
    def from_attributes(cls, obj):
        return cls(
            created_at=format_date(obj.created_at),
            updated_at=format_date(obj.updated_at)
            # deleted_at=format_date(obj.deleted_at)
        )

class DownloadCreate(BaseModel):
    url: str
    result: Optional[bool] = False 
    media_type: Optional[str] = 'audio'
    created_at: Optional[datetime] = None
    
class DownloadResponse(BaseTimestamp):
    id: int
    url: str
    result: bool
    # media_type: Optional[str] = 'audio'
    
    class Config:
        from_attributes = True
        
        @staticmethod
        def json_schema_extra(schema: dict, model):
            """
            Adjust the order of JSON's output fields.
            """
            schema["properties"] = OrderedDict(
                [
                    ("id", schema["properties"]["id"]),
                    ("url", schema["properties"]["url"]),
                    ("result", schema["properties"]["result"]),
                    ("createdAt", schema["properties"]["created_at"]),
                    ("updatedAt", schema["properties"]["updated_at"]),
                ]
            )
    
    @classmethod
    def from_sqlalchemy(cls, obj, media_type: str = 'audio'):
        """
        Converts an instance of Sqlalchemy to Pydantic. 
        """
        return cls(
            id = obj.id,
            url = obj.youtube_url,
            result = obj.result,
            media_type = media_type,
            created_at = format_date(obj.created_at),
            updated_at = format_date(obj.updated_at)
        )