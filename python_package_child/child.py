"""Implementation of Python Package Child."""
from .utils.greetings import say_hello


class Child:
    def __init__(self) -> None:
        """Create a new balenista."""
        self.label = 'balenista'

    def greet(self) -> None:
        """Introduce oneself."""
        print(f'{say_hello()}, I am {self.label}!')
