from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, MetaData
from typing import Optional, Dict
from core.db_core import Base

metadata: Optional[MetaData] = Base.metadata

class ChannelInfo(Base):
    __tablename__ = 'channel_info'

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    title: str = Column(String)
    description: Optional[str] = Column(Text)
    member_count: int = Column(Integer)
    link: Optional[str] = Column(String)


class LatestMessages(Base):
    __tablename__ = 'latest_messages'

    id: int = Column(Integer, primary_key=True, index=True)
    channel_id: int = Column(Integer, ForeignKey('channel_info.id'), index=True)
    date: Date = Column(Date)
    forwards: int = Column(Integer)
    url: str = Column(String)
    reactions: Optional[Dict[str, str]] = Column(String)
    text: str = Column(Text)
