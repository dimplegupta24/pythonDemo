def add(x, y):
    """Add  function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiplication function"""
    return x * y


def divide(x, y):
    """Division function"""
    if  y == 0:
        raise ValueError("Can't Divide by Zero!")
    return x / y 


# print("Addtion of numbers", add(10,5))


# print("Subtraction of numbers", subtract(10,5))


# print("Multiplication of numbers", multiple(10,5))
