
def find_negative(numbers: list[int]) -> int:
    """
    find_negative() is a function which accepts a list of integers
    and returns the first negative number found within the list.
    The function should return 0 when there are no negative numbers present.
        ex: [4, 7, -9, 11, 0] -> -9
        ex: [1, 2, 3, 14, 15] -> 0
    """
    
    i = 0 # set i equal to the first number in the list
    while i < len(numbers): # while i is less than the length of the numbers in the list
        if numbers[i] < 0: # if the numbers in the list of i is less than 0
            return numbers[i] # return the numbers that are less than 0
        i += 1 # move onto the next posiotion in the list if there is no negative present at first
    return 0