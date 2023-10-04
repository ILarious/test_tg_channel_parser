from typing import Optional

from sqlalchemy import Column, Integer, MetaData, String, Text
from sqlalchemy.dialects.postgresql import JSONB

from services.db.core import Base

metadata: Optional[MetaData] = Base.metadata


class ChannelInfo(Base):
    __tablename__ = 'channel_info'

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    title: str = Column(String)
    description: Optional[str] = Column(Text)
    member_count: int = Column(Integer)
    link: str = Column(String)
    messages: Optional[dict] = Column(JSONB)
