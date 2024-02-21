#!/usr/bin/python3

"""Square class with size and position attributes."""


class Square:
    """Initialize a Square object with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with proper positioning."""
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end="")
            print()
