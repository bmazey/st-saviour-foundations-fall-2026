
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    greatest = numbers[0] # setting the lowest to zero
    i = 0
    while i < len(numbers):
     if numbers[i] > 0:
        return len(numbers)

