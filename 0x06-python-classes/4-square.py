#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize square size.
    Args:
        size (int): size of the square
    """
    self.size = size

    @property
    def size(self):
        """get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
