
def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() is a function which accepts a list of integers
    and returns the greatest number found within the list.
        ex: [4, 7, 9, 11, 0] -> 11
    """

    greatest= numbers[0]
    i=0 # this is to show that i starts with the first number
    while i < len(numbers): # while the number it picks is larger than the length of number it will return the number you put in
        if numbers[i] > greatest:
            greatest= numbers[i]
        i +=1 #if the number is not greater than 0 then it will add to i to look at the other places until it finds one greater than 0 and it will then return greatest

    return greatest