from __future__ import annotations

import logging
from typing import Union, Mapping, cast, BinaryIO
from ..._types import FileTypes
from ..._utils import extract_files, required_args, maybe_transform, deepcopy_minimal
from ..._resource import SyncAPIResource
from ...types.audio import transcription_create_params
from ...types.audio.transcription import Transcription

__all__ = ["Transcriptions"]

log: logging.Logger = logging.getLogger("a4f.audio.transcriptions")


class Transcriptions(SyncAPIResource):
    @required_args(["file", "model"], ["file", "model"])
    def create(
        self,
        *,
        file: Union[bytes, BinaryIO],
        model: str,
    ) -> Transcription:
        """
        Transcribes an audio file into text.

        Args:
            file: File object (opened in binary mode) or bytes. Must be one of:
                  flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, webm.
            model: The transcription model to use. Example: 'provider-3/whisper-1'.

        Returns:
            Transcription object containing the transcription results.
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
            }
        )

        # Extract file handles for multipart/form-data
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        # Send POST request
        return self._post(
            "/audio/transcriptions",
            body=maybe_transform(
                body,
                transcription_create_params.TranscriptionCreateParams
            ),
            files=files,
            cast_to=Transcription
        )