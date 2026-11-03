
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    great = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > great:
            great = numbers[i]
        i += 1

    return great