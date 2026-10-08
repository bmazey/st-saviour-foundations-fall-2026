
def classify(price: float) -> str:
    """
    classify() is a function which accepts a float representing the price 
    of coffee and returns a string representing the brand:
      - return 'dunkin donuts' when price is greater than 0 and less than or equal to 5.0
      - return 'blank street' when price is greater than 5.0 and less than 11.0
      - return 'starbucks' when price is greater or equal to 11.0 and less than 17.50
      - return 'cafe paradiso' when price is 17.50 or greater
      - return 'error' when price is is 0 or less
    """
    # This explains what would be returned if the price if greater than 0 but less and or equal to 5
    if price > 0 and price  <= 5.0:
      return 'dunkin donuts'
    
    #This explains what would be returned if the price is greater than 5 but less than 11
    if price > 5.0 and price  < 11.0:
      return 'blank street'

    #This shows what would be returned if the price was greater than 11 but less than 17.50
    if price >= 11.0 and price < 17.50:
      return 'starbucks'

    #This shows what is returned if the price is greater than 17.50
    if price >= 17.50:
      return 'cafe paradiso'

    #This shows what would be returned if the price is less than or equal to 0
    if price <=0:
      return 'error'
    