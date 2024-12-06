from pydantic import BaseModel

class DownloadCreate(BaseModel):
    url: str
    successful: bool
    
class DownloadResponse(BaseModel):
    id: int
    url: str
    successful: bool
    
    class Config:
        from_attributes = True