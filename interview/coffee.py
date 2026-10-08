
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
    # the price of dunkin is >0 but <= 5
    if price > 0 and price <= 5.0:
      return 'dunkin donuts'
    # the price of blank street is >5 but <11
    if price > 5.0 and price < 11.0:
      return 'blank street'
    # the price of Starbucks is >=11 but <17.5
    if price >= 11.0 and price < 17.50:
       return 'starbucks'
    # the price of cafe paradiso is >=17.5
    if price >= 17.50:
       return 'cafe paradiso'
    # so store is just giving out coffee for free so if the price is <=0 the word error shows up
    if price <= 0:
       return 'error'

