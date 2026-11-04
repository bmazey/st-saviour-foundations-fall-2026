
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """
    # sum and i are equal to zero
    sum = 0
    i = 0
    # zero is less than numbers list
    while i < len(numbers): 
        sum += numbers[i]
        i += 1

    return sum
