from ..._models import BaseModel

__all__ = ["TranscriptionWord"]


class TranscriptionWord(BaseModel):
    end: float
    """End time of the word in seconds."""

    start: float
    """Start time of the word in seconds."""

    word: str
    """The text content of the word."""
