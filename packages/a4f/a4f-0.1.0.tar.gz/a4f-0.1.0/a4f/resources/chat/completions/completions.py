from __future__ import annotations
from typing import Union, Iterable, Optional, cast
from functools import partial

from .messages import Messages
from ...._types import NOT_GIVEN, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource
from ....types.chat import completion_create_params
from ....types.chat.chat_completion import ChatCompletion
from ....types.chat.chat_completion_chunk import ChatCompletionChunk
from ....types.chat.chat_completion_message_param import ChatCompletionMessageParam
from ....types.chat.chat_completion_tool_union_param import ChatCompletionToolUnionParam
from ....types.chat.chat_completion_stream_manager import ChatCompletionStreamManager

__all__ = ["Completions"]


class Completions(SyncAPIResource):
    @cached_property
    def messages(self) -> Messages:
        return Messages(self._client)

    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: str,
        stream: bool = False,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolUnionParam] | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | ChatCompletionStreamManager:

        payload = maybe_transform(
            {
                "messages": messages,
                "model": model,
                "function_call": function_call,
                "functions": functions,
                "max_tokens": max_tokens,
                "stream": stream,
                "temperature": temperature,
                "tools": tools,
            },
            completion_create_params.CompletionCreateParams,
        )

        if stream:
            return ChatCompletionStreamManager(
                api_request=partial(
                    self._post,
                    "/chat/completions",
                    body=payload,
                    cast_to=ChatCompletion,
                    stream=True,
                )
            )

        # Normal synchronous response
        return self._post(
            "/chat/completions",
            body=payload,
            cast_to=ChatCompletion,
            stream=False,
        )