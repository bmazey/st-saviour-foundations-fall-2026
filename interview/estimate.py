
from unicodedata import decimal


def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

# example 7.5 -> .5 example 3.1 -> .1
    decimal = number % 1 
    if decimal >= 0.5:
        return int(number) + 1


    return int(number)
