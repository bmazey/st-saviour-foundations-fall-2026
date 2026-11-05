
def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() is a function which accepts a list of integers
    and returns a new list containing only even numbers found in the origial.
    The returned list should preserve the original order.
        ex: [2, 7, 12, 1, 10] -> [2, 12, 10]
    """
    # create a list called evens
    evens = []
    # when i is in equal to the first position in the list
    i = 0
    # when i is less than the length of the numbers...
    while i < len(numbers):
        # if the numbers in the list equal zero when modulo two
        if numbers[i] % 2 == 0:
            evens.append (numbers[i])
        i += 1
        return evens