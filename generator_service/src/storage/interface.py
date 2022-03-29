from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class ErrorStoreException(Exception):
    """Error store data exception."""


@dataclass
class TickerData:
    """Ticker data model."""
    name: str
    value: float


class StorageInterface(ABC):
    """Interface for ticker data storage."""

    @abstractmethod
    def store(self, tickers: List[TickerData]):
        """Store ticker data."""
        pass
