from typing import List, Optional

from pydantic import BaseModel

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
