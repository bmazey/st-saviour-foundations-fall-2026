
def find_negative(numbers: list[int]) -> int:
    """
    find_negative() is a function which accepts a list of integers
    and returns the first negative number found within the list.
    The function should return 0 when there are no negative numbers present.
        ex: [4, 7, -9, 11, 0] -> -9
        ex: [1, 2, 3, 14, 15] -> 0
    """
    i = 0 # this means that it will start at position 0
    while i < len(numbers): # this basically is saying that while i or the number it is picking is less than zero then it will return the number but if its not less than 0 it will add 1 to i to see if the next number is 0 this is for lines 11-14
        if numbers[i] < 0:
            return numbers[i]
        i += 1
    return 0 # this means that each time it runs if there is no negative number it will return 0

        
g