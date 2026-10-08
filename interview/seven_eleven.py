
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """
    # this shows what would happen if a number is a multiple of both 7 and 11
    if number % 7 == 0 and number % 11 ==0:
        return 'seveneleven'

    # This shows what would return if the number is a multiple of seven
    if number % 7 == 0:
        return 'seven'

    # This shows what would be returned if the number is a multiple of 11
    if number % 11 == 0:
        return 'eleven'

    # This shows what would be returned if the number is not a multiple of 7 or 11
    if number % 7 != 0 and number % 11 !=0:
        return ''



