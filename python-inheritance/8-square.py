"""Creates a Square class."""
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py)
    Private instance attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a Square.
        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2