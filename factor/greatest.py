
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    greatest = numbers[0]
    #Start loop at the first index
    i = 0
    #Loop through all list items
    while i < len[numbers][i]:
        if [numbers][i] > greatest:
            greatest = [numbers][i]
        i += 1
    return greatest