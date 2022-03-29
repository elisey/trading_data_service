from abc import ABC, abstractmethod


class TickerAbstract(ABC):
    """
    Abstract ticker.

    Additional logic for price generation can be added
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_value(self) -> float:
        """Get ticker value."""
        pass

    def get_name(self):
        """Get ticker name."""
        return self.name
