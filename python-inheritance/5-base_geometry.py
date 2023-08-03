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
