from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TimestampMixin():
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class Download(Base, TimestampMixin):
    __tablename__ = 'downloads'
    id = Column(Integer, primary_key=True, index=True)
    youtube_url = Column(String(255), nullable=False)
    youtube_id = Column(String(20), nullable=False)
    title = Column(String(100), nullable=False)
    fulltitle = Column(String(100), nullable=False)
    uploader = Column(String(50), nullable=False)
    channel = Column(String(50), nullable=False)
    duration = Column(String(5), nullable=False)
    label = Column(String(25), nullable=False)
    copyright = Column(String(25), nullable=False)
    origin_url = Column(String(255), nullable=False)
    live_status = Column(String(10), nullable=False)
    extractor = Column(String(25), nullable=False)
    categories = Column(String(25), nullable=False)
    result = Column(Boolean, default=False)