
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    greatest = numbers[0]
    #telling python to start at the first position in the list
    i = 0
    #loop is saying while i is less than the legnth of numbers it will move to the next posiiton until i is greater than the legnth
    while i < len(numbers):
        if numbers[i] > greatest:
            greatest = numbers[i]
        i += 1

    return greatest