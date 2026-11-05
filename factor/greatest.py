
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    # create a variable that points to the first item in the list
    greatest = numbers[0]

    i = 0 
    while i < len(numbers):
        # if the number we're on is bigger, update greatest 
        if numbers[i] > greatest:
            greatest = numbers[i]
        i += 1

    return greatest