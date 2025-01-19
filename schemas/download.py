from collections import OrderedDict
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl

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


class DownloadRequest(BaseModel):
    url: str
    audio: bool = Field(default=True)


class DownloadCreate(BaseModel):
    url: str
    youtube_id: Optional[str] = ''
    title: Optional[str] = ''
    fulltitle: Optional[str] = ''
    uploader: Optional[str] = ''
    channel: Optional[str] = ''
    duration: Optional[str] = ''
    label: Optional[str] = ''
    copyright: Optional[str] = ''
    origin_url: Optional[str] = ''
    live_status: Optional[str] = ''
    extractor: Optional[str] = ''
    categories: Optional[str] = ''
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
                    ("youtube_id", schema["properties"]["youtube_id"]),
                    ("title", schema["properties"]["title"]),
                    ("fulltitle", schema["properties"]["fulltitle"]),
                    ("uploader", schema["properties"]["uploader"]),
                    ("channel", schema["properties"]["channel"]),
                    ("duration", schema["properties"]["channel"]),
                    ("label", schema["properties"]["label"]),
                    ("copyright", schema["properties"]["copyright"]),   
                    ("origin_url", schema["properties"]["origin_url"]),
                    ("live_status", schema["properties"]["live_status"]),
                    ("extractor", schema["properties"]["extractor"]),
                    ("categories", schema["properties"]["categories"]),    
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
            youtube_id = obj.youtube_id,
            title = obj.title,
            fulltitle = obj.fulltitle,
            uploader = obj.uploader,
            channel = obj.channel,
            duration = obj.duration,
            label = obj.label,
            copyright = obj.copyright,
            origin_url = obj.origin_url,
            live_status = obj.live_status,
            extractor = obj.extractor,
            categories = obj.categories,
            result = obj.result,
            media_type = media_type,
            created_at = format_date(obj.created_at),
            updated_at = format_date(obj.updated_at)
        )