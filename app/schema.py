from typing import List
from pydantic import BaseModel

class CreateChatInput(BaseModel):
    chat_name: str
    users: List[str]

class OkOutput(BaseModel):
    ok: bool
