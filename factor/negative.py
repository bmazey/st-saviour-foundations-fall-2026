
def find_negative(numbers: list[int]) -> int:
    """
    find_negative() is a function which accepts a list of integers
    and returns the first negative number found within the list.
    The function should return 0 when there are no negative numbers present.
        ex: [4, 7, -9, 11, 0] -> -9
        ex: [1, 2, 3, 14, 15] -> 0
    """

    i=0 #starting at the first thing on the list
    while  i < len(numbers): #while the number is in the list
        if numbers[i] < 0: #checking for a negative number
            return numbers[i] #returns a number if its negative
        i += 1 #if number isnt negative it moves on to the next number on the list, repeat from start
    return 0 #once i > len(numbers), zero will be returned, showing that there are no negatives