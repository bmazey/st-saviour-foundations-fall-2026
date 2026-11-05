
def find_negative(numbers: list[int]) -> int:
    """
    find_negative() is a function which accepts a list of integers
    and returns the first negative number found within the list.
    The function should return 0 when there are no negative numbers present.
        ex: [4, 7, -9, 11, 0] -> -9
        ex: [1, 2, 3, 14, 15] -> 0
    """

    # address the case were numbers is empty 
    if len(numbers) == 0:
        return 0
    
    for n in numbers:
        # check if n is negative
        if n < 0:
            return n

    return 0
