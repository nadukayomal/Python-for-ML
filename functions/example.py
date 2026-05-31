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

"""
    Name argument
        - if we add name argument to the function , all other argument should be named argument and put the right side 
"""

def brand_price_1(brand, price):
    print(brand)
    if price >= 1000:
        print("gold")
    elif price >= 500:
        print("silver")
    else:
        print("bronz")

brand_price_1(brand='Toyota', price=100000)
# brand_price_1(brand='Toyota', 100000) # occur some error
brand_price_1('Toyota', price=100000)


"""
    Packed args & Kwargs
        - We passed the too many parameter to the same argument
        - We can use packed and kwargs in same function but.
            always should keep kwargs after the packed
"""
# this is packed
def get_grade(*marks):
    total = 0
    for i in marks:
        total += 1
    print(total)

get_grade(10, 20, 30)

# this is kwarg
def my_form(**params):
    print(params)

my_form(name="John", city="New York", age=23)


