from typing import List
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl

class Voice(str, Enum):
    ALLOY = "alloy"
    ASH = "ash"
    BALLAD = "ballad"
    CORAL = "coral"
    ECHO = "echo"
    FABLE = "fable"
    NOVA = "nova"
    ONYX = "onyx"
    SAGE = "sage"
    SHIMMER = "shimmer"

class Role(str, Enum):
    SENDER = "sender"
    RECEIVER = "receiver"

class Character(str, Enum):
    HUSBAND = "husband"
    WIFE = "wife"

class Message(BaseModel):
    role: Role | Character
    text: str = Field(..., min_length=1)

class Voices(BaseModel):
    sender: Voice
    receiver: Voice

class Clip(BaseModel):
    url: HttpUrl
    duration_ms: int = Field(..., ge=0)

class ChatRequest(BaseModel):
    messages: List[Message]
    voices: Voices

class ChatResponse(BaseModel):
    clips: List[Clip]
    voices: Voices

class LineRequest(BaseModel):
    text: str = Field(..., min_length=1)
    voice: Voice

class LineResponse(BaseModel):
    clip: Clip

class ChatMessages(BaseModel):
    messages: List[Message]
    hubb_index: int
