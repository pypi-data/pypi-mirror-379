from __future__ import annotations

import asyncio
import os
from typing import Optional

import openai
from openai import AsyncOpenAI
from openai import OpenAI

from amsdal_ml.ml_config import ml_config
from amsdal_ml.ml_models.models import MLModel
from amsdal_ml.ml_models.models import ModelAPIError
from amsdal_ml.ml_models.models import ModelConnectionError
from amsdal_ml.ml_models.models import ModelError
from amsdal_ml.ml_models.models import ModelRateLimitError


class OpenAIModel(MLModel):
    def __init__(self):
        self.client: Optional[OpenAI | AsyncOpenAI] = None
        self.async_mode: bool = bool(ml_config.async_mode)
        self.model_name: str = ml_config.llm_model_name
        self.temperature: float = ml_config.llm_temperature
        self._api_key: Optional[str] = None

    def setup(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY") or ml_config.resolved_openai_key
        if not api_key:
            msg = (
                "OPENAI_API_KEY is required. "
                "Set it via env or ml_config.api_keys.openai."
            )
            raise RuntimeError(msg)
        self._api_key = api_key

        try:
            if self.async_mode:
                try:
                    asyncio.get_running_loop()
                    self._ensure_async_client()
                except RuntimeError:
                    self.client = None
            else:
                self.client = OpenAI(api_key=self._api_key)
        except Exception as e:
            raise self._map_openai_error(e) from e

    def _ensure_async_client(self) -> None:
        if self.client is None:
            try:
                self.client = AsyncOpenAI(api_key=self._api_key)
            except Exception as e:
                raise self._map_openai_error(e) from e

    def teardown(self) -> None:
        self.client = None

    @staticmethod
    def _map_openai_error(err: Exception) -> ModelError:
        if isinstance(err, openai.RateLimitError):
            return ModelRateLimitError(str(err))

        if isinstance(err, openai.APIConnectionError):
            return ModelConnectionError(str(err))

        if isinstance(err, openai.APIStatusError):
            status = getattr(err, "status_code", None)
            resp = getattr(err, "response", None)
            payload_repr = None
            try:
                payload_repr = resp.json() if resp is not None else None
            except Exception:
                payload_repr = None
            msg = f"OpenAI API status error ({status}). payload={payload_repr!r}"
            return ModelAPIError(msg)

        if isinstance(err, openai.APIError):
            return ModelAPIError(str(err))

        return ModelAPIError(str(err))

    # ---------- Sync ----------
    def invoke(self, prompt: str) -> str:
        if self.async_mode:
            msg = "Async mode is enabled. Use 'ainvoke' instead."
            raise RuntimeError(msg)

        if not isinstance(self.client, OpenAI):
            msg = "Sync client is not initialized. Call setup() first."
            raise RuntimeError(msg)

        try:
            resp = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            raise self._map_openai_error(e) from e

    def stream(self, prompt: str):
        if self.async_mode:
            msg = "Async mode is enabled. Use 'astream' instead."
            raise RuntimeError(msg)

        if not isinstance(self.client, OpenAI):
            msg = "Sync client is not initialized. Call setup() first."
            raise RuntimeError(msg)

        try:
            stream = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    yield delta.content
        except Exception as e:
            raise self._map_openai_error(e) from e

    # ---------- Async ----------
    async def ainvoke(self, prompt: str) -> str:
        if not self.async_mode:
            msg = "Async mode is disabled. Use 'invoke' instead."
            raise RuntimeError(msg)

        self._ensure_async_client()
        if not isinstance(self.client, AsyncOpenAI):
            msg = "Async client is not initialized. Call setup() first."
            raise RuntimeError(msg)

        client = self.client
        try:
            resp = await client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            raise self._map_openai_error(e) from e

    async def astream(self, prompt: str):
        if not self.async_mode:
            msg = "Async mode is disabled. Use 'stream' instead."
            raise RuntimeError(msg)

        self._ensure_async_client()
        if not isinstance(self.client, AsyncOpenAI):
            msg = "Async client is not initialized. Call setup() first."
            raise RuntimeError(msg)

        client = self.client
        try:
            stream = await client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                stream=True,
            )
            async for chunk in stream:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    yield delta.content
        except Exception as e:
            raise self._map_openai_error(e) from e
