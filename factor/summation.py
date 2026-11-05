
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """
    # setting summation the first number in the list
    sum = 0
    # index is set to start from the first number in the list
    i = 0
    # when i is less than the length of numbers in the list
    while i < len(numbers):
    # take the numbers we are at and add that to the sum
        sum += numbers[i]
    # now increase i's position by one
        i+= 1    

    return sum