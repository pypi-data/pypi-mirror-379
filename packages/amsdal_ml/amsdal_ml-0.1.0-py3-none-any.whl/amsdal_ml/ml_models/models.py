from abc import ABC
from abc import abstractmethod


class ModelError(Exception):
    """Base exception for all ML models."""


class ModelConnectionError(ModelError):
    """Network or connection failure to the provider (timeouts, DNS, TLS, etc.)."""


class ModelRateLimitError(ModelError):
    """Provider's rate limit reached (HTTP 429)."""


class ModelAPIError(ModelError):
    """API responded with an error (any 4xx/5xx, except 429)."""


class MLModel(ABC):
    @abstractmethod
    def setup(self):
        """Initialize any clients or resources needed before inference."""
        pass

    @abstractmethod
    def teardown(self):
        """Clean up resources after use."""
        pass

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        """Run synchronous inference with the model."""
        pass

    @abstractmethod
    async def ainvoke(self, prompt: str) -> str:
        """Run asynchronous inference with the model."""
        pass

    @abstractmethod
    def stream(self, prompt: str):
        """Stream synchronous inference results from the model."""
        pass

    @abstractmethod
    async def astream(self, prompt: str):
        """Stream asynchronous inference results from the model."""
        pass
