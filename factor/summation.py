
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    # TODO

    sum = 0 
    i = 0 # this means that it will start with position 0
    while i < len(numbers): # meaning that it will stay in the number range
        sum += numbers[i]
        i+=1 # will continue adding to i

    return sum # will give back the sum if correct