
def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() is a function which accepts a list of integers
    and returns a new list containing only even numbers found in the origial.
    The returned list should preserve the original order.
        ex: [2, 7, 12, 1, 10] -> [2, 12, 10]
    """

    evennumbers = []

    # if [] is not numbers return [] 
    if not numbers: 
        return []
    
    for number in numbers:
        # if number modelo 2 it equals 0 
        if number % 2 == 0:
            evennumbers.append(number)

    return evennumbers
