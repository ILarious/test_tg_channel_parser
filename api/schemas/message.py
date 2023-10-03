from pydantic import BaseModel
from typing import Optional, List

from api.schemas.reactions import ReactionPydantic


class LatestMessagePydantic(BaseModel):
    id: int
    channel_id: int
    views: int
    date: str
    forwards: int
    url: str
    reactions: Optional[List[ReactionPydantic]]
    message_text: str
