
def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() is a function which accepts a list of integers
    and returns a new list containing only even numbers found in the origial.
    The returned list should preserve the original order.
        ex: [2, 7, 12, 1, 10] -> [2, 12, 10]
    """

    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            print (numbers[i])
        i += 1
        