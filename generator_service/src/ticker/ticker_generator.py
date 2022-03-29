from movement_generator.interface import MovementGeneratorInterface
from ticker.abstract import TickerAbstract


class TickerGenerator(TickerAbstract):
    """Ticker, which can generate new value by using Generator object."""

    def __init__(self, name: str, generator: MovementGeneratorInterface):
        super().__init__(name)
        self.generator = generator

    def get_value(self) -> float:
        """Get ticker value."""
        return self.generator.generate()
