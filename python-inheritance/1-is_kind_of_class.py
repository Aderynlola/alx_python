"""
a function defining an object to be a kind of the specified class
"""
def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from, the specified class
    otherwise False.
    """
    return isinstance(obj, a_class)