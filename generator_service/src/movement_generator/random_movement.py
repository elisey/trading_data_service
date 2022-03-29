from random import random

from movement_generator.interface import MovementGeneratorInterface


class RandomMovementGenerator(MovementGeneratorInterface):
    def __init__(self):
        self.current_value: float = 0.0

    @staticmethod
    def __generate_movement() -> float:
        """Random price generator."""
        return -1 if random() < 0.5 else 1

    def generate(self) -> float:
        """Generate new price."""
        self.current_value = self.current_value + RandomMovementGenerator.__generate_movement()
        return self.current_value
