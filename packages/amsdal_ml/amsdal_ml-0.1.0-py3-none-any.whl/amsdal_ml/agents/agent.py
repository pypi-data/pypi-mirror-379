from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import AsyncIterator
from collections.abc import Iterator
from typing import Any
from typing import Literal

from pydantic import BaseModel
from pydantic import Field


class AgentMessage(BaseModel):
    role: Literal["SYSTEM", "USER", "ASSISTANT"]
    content: str


class AgentOutput(BaseModel):
    answer: str
    used_tools: list[str] = Field(default_factory=list)
    citations: list[dict[str, Any]] = Field(default_factory=list)


class Agent(ABC):
    @abstractmethod
    async def arun(self, user_query: str) -> AgentOutput: ...
    @abstractmethod
    async def astream(self, user_query: str) -> AsyncIterator[str]:
        """Yield streamed chunks for the given query."""
        raise NotImplementedError

    def run(self, user_query: str) -> AgentOutput:
        msg = "This agent is async-only. Use arun()."
        raise NotImplementedError(msg)

    def stream(self, user_query: str) -> Iterator[str]:
        msg = "This agent is async-only. Use astream()."
        raise NotImplementedError(msg)
