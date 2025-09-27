from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletionDeleted"]


class ChatCompletionDeleted(BaseModel):
    id: str
    """The ID of the chat completion that was deleted."""

    deleted: bool
    """Whether the chat completion was deleted."""

    object: Literal["chat.completion.deleted"]
    """The type of object being deleted."""
