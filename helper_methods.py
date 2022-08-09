"""helper methods module"""
def isinstanceorsubclass(__obj: object, __class: type):
    """Check if objects is instance or subclass of type"""
    return isinstance(__obj, __class) or issubclass(__obj.__class__, __class)
