from typing import Literal, Annotated
from pydantic import BaseModel, Field, HttpUrl

Voice = Literal["alloy", "ash", "ballad", "coral", "echo", "fable", "nova", "onyx", "sage", "shimmer"]
Role = Literal["sender", "receiver"]
Text = Annotated[str, Field(min_length=1)]

class Message(BaseModel):
    role: Role
    text: Text

class ChatRequest(BaseModel):
    messages: list[Message]
    sender_voice: Voice = Field(alias="senderVoice")
    receiver_voice: Voice = Field(alias="receiverVoice")

class LineRequest(BaseModel):
    text: Text
    voice: Voice

class MultilingualMessage(BaseModel):
    role: Role
    en: Text = Field(description="English text")
    ar: Text = Field(description="Arabic text")

class MultilingualChat(BaseModel):
    messages: list[MultilingualMessage]
    highlight_index: int = Field(alias="highlightIndex")

class MessageAudio(BaseModel):
    url: str
    duration_ms: int = Field(serialization_alias="durationMs")

class MessageRequest(BaseModel):
    sentiment: str
    num_messages: int = Field(alias="numMessages")
    user_prompt: str = Field(alias="userPrompt")
    system_prompt: str = Field(alias="systemPrompt")
    