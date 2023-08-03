"""
a function defining an object that inherits from the specified class
"""
def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class 
    that inherited (directly or indirectly) from the specified class 
    otherwise False
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class)