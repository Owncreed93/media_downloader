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
    result = Column(Boolean, default=False)