
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # check if number has a factor of both seven and eleven
    if number % 7 == 0 and number % 11 == 0:
        return 'seveneleven'
    # check if number has a factor of seven
    if number % 7 == 0:
        return 'seven'
    # check if number has a factor of eleven
    if number % 11 == 0:
        return 'eleven'
    
    return ''
    