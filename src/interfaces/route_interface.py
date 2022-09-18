from abc import ABC, abstractmethod
from typing import Any


class IApiRoute(ABC):
    """API route interface."""

    @abstractmethod
    def request(*args: Any) -> Any:
        """API requester."""
        