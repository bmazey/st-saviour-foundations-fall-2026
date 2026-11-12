
def find_negative(numbers: list[int]) -> int:
    """
    find_negative() is a function which accepts a list of integers
    and returns the first negative number found within the list.
    The function should return 0 when there are no negative numbers present.
        ex: [4, 7, -9, 11, 0] -> -9
        ex: [1, 2, 3, 14, 15] -> 0
    """

    # TODO
    negative = numbers[0] # setting the base to zero
    i = 1 # setting i to 1 allows emliminations to occur which 
    while i < len(numbers):
        if numbers[i] < 0:
            return numbers[i]
        i += 1 # this causes other options to be eliminated
    return 0 
