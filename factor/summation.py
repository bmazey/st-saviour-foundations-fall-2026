
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    sum = 0
    i = 0
    while i < len(numbers): # len is the amount of the sum of all nums in the list 
        sum += numbers [i]
        i += 1 
    return sum # finding the sum of all numbers