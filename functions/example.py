def assign_marks(mark):
    if mark >= 75:
        mark = 'A'
    elif mark >= 55:
        mark = "B"
    else:
        mark = "c-"
    return mark

get_mark = assign_marks(40)
print(get_mark)


""" 
    Positional parameter 
        - We need to pass the values as we defined order
        - We can't define argument after positional parameter
"""

def brand_price(brand, price):
    print(brand)
    if price >= 1000:
        print("gold")
    elif price >= 500:
        print("silver")
    else:
        print("bronz")


brand_price("apple", 100)
# brand_price("apple", '100') # this occur an error