from sqlalchemy import Column, Integer, String, Text, MetaData
from typing import Optional

from sqlalchemy.dialects.postgresql import JSONB

from services.db.db_core import Base

metadata: Optional[MetaData] = Base.metadata


class ChannelInfo(Base):
    __tablename__ = 'channel_info'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
    member_count = Column(Integer)
    link = Column(String)
    messages = Column(JSONB)