
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    sum = 0
    i = 0 
    #the while loop is saying while i is less than the legnth continue the loop
    while i < len(numbers):
        sum += numbers[i]
        i += 1 
    #this reutn is saying to return all the numbers on the list added
    return sum