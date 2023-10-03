from pydantic import BaseModel, HttpUrl
from typing import Optional, List

from api.schemas.message import LatestMessagePydantic


class ChannelInfo(BaseModel):
    id: int
    title: str
    username: str
    description: Optional[str] = None
    member_count: int
    link: HttpUrl
    messages: Optional[List[LatestMessagePydantic]]


class ChannelInfoPydantic(BaseModel):
    id: int
    title: str
    username: str
    description: Optional[str] = None
    member_count: int
    link: HttpUrl
