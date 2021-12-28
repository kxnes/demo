"""Main application."""
import enum


class Animal(enum.Enum):
    """Registered animal types."""

    dog = 'bark'
    cat = 'meow'


def sound(animal: Animal) -> str:
    """
    Return how the `animal` can sound.

    :param animal: animal type

    :return: animal sound
    """
    return animal.value
