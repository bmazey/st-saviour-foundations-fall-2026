
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """
    # created a variable and set it equal to the first number in the list
    greatest = numbers[0]
    # i is equal to the dirst number in the list
    i = 0
    # when i is less than the length of numbers...
    while i < len(numbers):
    # when numbers is in position i and geater than the greatest
        if numbers[i] > greatest:
    # greatest is equal to the number in position i
            greatest = numbers[i]
    # i is increased by one position
        i += 1
    return greatest