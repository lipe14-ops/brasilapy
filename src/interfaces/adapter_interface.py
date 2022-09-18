from abc import ABC, abstractstaticmethod
from typing import Any


class IAdapter(ABC):
    """adapter interface"""

    @abstractstaticmethod
    def handler(*args: Any) -> Any:
        """data adapter handler."""
