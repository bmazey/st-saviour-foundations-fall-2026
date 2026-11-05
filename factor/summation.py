
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    sum = 0 #sum before running loop
    i = 0 #number to start at in the list
    while i < len(numbers): #while it is in the list continue to the next thing
        sum += numbers[i] #take the previous sum and add the current number on the list
        i += 1 #continue to the next thing on the list

    return sum #once all things from the list are added, return the sum.