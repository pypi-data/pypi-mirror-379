from __future__ import annotations

from typing import Union, Mapping, Optional, Sequence, cast, TypeVar, BinaryIO
from typing_extensions import Literal

from ..types import image_edit_params, image_generate_params
from .._types import NOT_GIVEN
from .._utils import extract_files, required_args, maybe_transform, deepcopy_minimal
from .._resource import SyncAPIResource
from ..types.images_response import ImagesResponse
from ..types.image_gen_stream_event import ImageGenStreamEvent
from ..types.image_edit_stream_event import ImageEditStreamEvent

__all__ = ["Images"]

# Type hints
FileTypes = Union[bytes, "BinaryIO"]  # file handle or bytes
T = TypeVar("T")
SequenceNotStr = Sequence[T]  # generic sequence of items

class Images(SyncAPIResource):
    @required_args(["image", "prompt", "model"], ["image", "prompt", "model"])
    def edit(
        self,
        *,
        image: Union[FileTypes, SequenceNotStr[FileTypes]],
        prompt: str,
        model: str,
        response_format: Optional[Literal["url", "b64_json"]] = "url",
        user: Optional[str] = None,
    ) -> ImagesResponse:
        """
        Edit an existing image based on a text prompt.

        Args:
            image: File handle, bytes, or sequence of files to edit.
            prompt: Text description of the desired edit.
            model: ID of the image editing model (must include provider prefix).
            response_format: "url" (default) or "b64_json".
            user: Optional user identifier.

        Returns:
            ImagesResponse
        """

        # Build request body
        body = deepcopy_minimal(
            {
                "image": image,
                "prompt": prompt,
                "model": model,
                "response_format": response_format,
                "user": user,
            }
        )

        # Extract file handles for multipart/form-data
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])

        # Send POST request
        return self._post(
            "/images/edits",
            body=maybe_transform(body, image_edit_params.ImageEditParams),
            files=files,
            cast_to=ImagesResponse,
        )

    @required_args(["prompt", "model"], ["prompt", "model"])
    def generate(
        self,
        *,
        prompt: str,
        model: str,
        n: Optional[int] = NOT_GIVEN,
        quality: Optional[Literal["standard", "hd"]] = NOT_GIVEN,
        response_format: Optional[Literal["url", "b64_json"]] = NOT_GIVEN,
        size: Optional[
            Literal["1024x1024", "256x256", "512x512", "1792x1024", "1024x1792"]
        ] = NOT_GIVEN,
        style: Optional[Literal["vivid", "natural"]] = NOT_GIVEN,
        user: Optional[str] = NOT_GIVEN,
    ) -> ImagesResponse:
        """
        Generate images from a text prompt.

        Args:
            prompt: Text description of the desired image.
            model: ID of the image generation model.
            n: Number of images to generate.
            quality: "standard" or "hd".
            response_format: "url" (default) or "b64_json".
            size: Dimensions of the output image.
            style: Optional style ("vivid" or "natural").
            user: Optional user identifier.

        Returns:
            ImagesResponse
        """
        body = maybe_transform(
            {
                "prompt": prompt,
                "model": model,
                "n": n,
                "quality": quality,
                "response_format": response_format,
                "size": size,
                "style": style,
                "user": user,
            },
            image_generate_params.ImageGenerateParams,
        )

        return self._post(
            "/images/generations",
            body=body,
            cast_to=ImagesResponse,
        )