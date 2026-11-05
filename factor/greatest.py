
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    greatest = numbers[0] #the starting number
    i=0 #the staring point in the list
    while i < len(numbers): #if its in the list do the next thing
        if numbers [i] > greatest: #checking if its bigger than the previous number
            greatest = numbers[i] #setting the greatest number so far to be the greatest
        i += 1 #moveing on tho the next item on the list
    
    return greatest #continue the loop, and return the greatest when finished