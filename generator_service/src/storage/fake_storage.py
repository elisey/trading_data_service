import logging
from typing import List

from storage.interface import StorageInterface, TickerData


class FakeStorage(StorageInterface):
    """Fake data storage."""

    def store(self, tickers: List[TickerData]):
        """Print stored data to log."""
        for ticker in tickers:
            logging.info(ticker)
