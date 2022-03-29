from abc import ABC, abstractmethod


class MovementGeneratorInterface(ABC):
    """Interface for the price change generator."""

    @abstractmethod
    def generate(self) -> float:
        """Generate new price."""
        pass
