"""defining a class BaseGeometry"""
class BaseGeometry:
    """a base class for geometrical operations"""
    def area(self):
        """calculates area of the geometry
        raises Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate if the value is an integer greater than 0.

        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
        
class Rectangle(BaseGeometry):
    """
    class Rectangle inherits from class BaseGeometry.

    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.

    __init__(self, width, height): Initializes a Rectangle object with the specified width and height.
    __str__(self): Returns a string representation of the Rectangle object.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with the specified width and height.

        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns a string containing the width and height of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        """
        Calculates the area of the rectangle.

        Returns the area of the rectangle.
        """
        return self.__width * self.__height
    
class Square(Rectangle):
    """
    class Square,inherits from class Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square object with the specified size.
    """

    def __init__(self, size):
        """
        Initialize a Square object with the specified size.

        size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less or equal to 0.
        """
        super().__init__(size, size)

