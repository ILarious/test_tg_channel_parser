from pydantic import BaseModel
from typing import Optional


class ChannelInfo(BaseModel):
    id: int
    username: str
    title: str
    description: Optional[str] = None
    member_count: int
    link: str
    messages: Optional[list] = list