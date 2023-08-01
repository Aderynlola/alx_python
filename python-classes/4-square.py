"""This module defines a Square class.
The Square class represents a square with a private instance attribute 'size'.
It allows instantiation with an optional size,
and provides methods to calculate the square's area and print the square.
The size attribute can be accessed using a property 'size'
with a setter for validation.
"""
class Square:
    """A class representing a square.
    Attributes:
        __size (int): The size of the square.

    Methods:
        _init_(self, size=0): Initializes square obj with optional size.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character '#'.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square.
        The size must be an integer, and >= 0

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)