"""
a function defining an object to be an instance of the specified class
"""
def is_same_class(obj, a_class):
    """returning true if the object is an instance of the specified class"""
    return type(obj) is a_class