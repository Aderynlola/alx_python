""" defining class square """
class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square attributes
        """
        self.__size = size

    @property
    def size(self):
        """ getting the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the value of size to be an integer
        and less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """getting the area using the size value"""
        return self.__size*self.__size