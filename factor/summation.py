
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    sum = 0 
    # if i equals zero then we start at zero 
    i = 0 
    while i < len(numbers):
        # sum 
        sum += numbers[i]
        # i is plus or equal to one meaning i starts at one 
        i += 1 

    return sum
