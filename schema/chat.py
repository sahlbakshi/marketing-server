from typing import Literal, Annotated
from pydantic import BaseModel, Field, HttpUrl

Voice = Literal["alloy", "ash", "ballad", "coral", "echo", "fable", "nova", "onyx", "sage", "shimmer"]
Role = Literal["sender", "receiver"]
Character = Literal["husband", "wife"]
Text = Annotated[str, Field(min_length=1)]

class Message(BaseModel):
    role: Role
    text: Text

class Clip(BaseModel):
    url: HttpUrl
    duration_ms: int

class ChatRequest(BaseModel):
    messages: list[Message]
    voices: dict[Role, Voice]

class ChatResponse(BaseModel):
    clips: list[Clip]

class LineRequest(BaseModel):
    text: Text
    voice: Voice

class LineResponse(BaseModel):
    clip: Clip

class MultilingualMessage(BaseModel):
    role: Character
    text: dict[str, Text]

class MultilingualChatResponse(BaseModel):
    messages: list[MultilingualMessage]
    highlight_index: int
