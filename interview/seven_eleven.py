
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """
    # this shows 'seveneleven' if the number is both a multiple of 7 and 11
    if number % 7 == 0 and number % 11 == 0:
      return 'seveneleven'  
    # this shows 'seven' if the number is a multiple of 7
    if number % 7 == 0:
        return 'seven'
    # this shows 'eleven' if the number is a multiple of 11
    if number % 11 == 0:
        return 'eleven'
    #this shows an empty string ('') if the number is neither 7 nor 11
    if number % 7 != 0 and number % 11 != 0:
        return ''


