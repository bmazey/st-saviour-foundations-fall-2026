
def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() is a function which accepts a list of integers
    and returns a new list containing only even numbers found in the origial.
    The returned list should preserve the original order.
        ex: [2, 7, 12, 1, 10] -> [2, 12, 10]
    """

    evens = []
    i = 0
    while i < len(numbers):
        #the modulo is saying that if you remove every two from a number and it queals 0 return that number
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
        #This is simply saying to move to the next position when done
        i += 1

    return evens
