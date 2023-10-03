from pydantic import BaseModel


class ReactionPydantic(BaseModel):
    emoticon: str
    count: int
