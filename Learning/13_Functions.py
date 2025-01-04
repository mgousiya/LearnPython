# function = a block of reusable code
#            place () after the function name to invoke it
# There are four types of parameters in python
# 1. Positional Parameters
# 2. Keyword Parameters
# 3. Default Parameters
# 4. Variable-length Parameters

## POSITIONAL ARGUMENTS: examples
#Happy Birthday song
# in the below ex (name, age) are parameters 
# in print statement we are giving arguments
""" def happy_birthday(name, age):
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old")
    print("Happy Birthday to you")
    print()

happy_birthday("emily", 8) """

# Due Example
""" 
def display_invoice(user_name,due_amount,due_date):
    print(f"Hello {user_name}")
    print(f"Your bill of ${due_amount: .2f} on {due_date} ")

display_invoice("Joe",35,"03/04")
 """

## return = statement used to end a function
#          and send back a result to the caller
""" 
def add(a,b):
    c = a + b
    return c
print(add(1, 2)) """

""" def substract(a,b):
    c = a - b
    return c
print(substract(1, 2)) """

""" def divide(a,b):
    c = a/b
    return c
print(divide(4, 2)) """

""" def multiply(a,b):
    c = a * b
    return c
print(multiply(2, 4)) """

""" def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("selena","Gomez")
print(full_name) """

##3.  DEFAULT ARGUMENTS: A default value for a certain parameter default is used when  that argument is omitted make 
#                     your functions more flexible, reduces # of arguments
# In default parameters, we can give default values to the parameters instead of giving arguments


""" def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount)  * (1 + tax)
print(500)
 """
""" 
import time
def count(start, end):
    for x in range (start, end+1):
        print(x)
        time.sleep(1)
    print("Done")
count(0,10) """

## 2. KEYWORD ARGUMENTS:

# keyword = keyword precided by an identifier helps with readability  order of arguments does not matter.
# positional argument follows keyword argument
# end = "" is a keyword argument in the print function

""" 
def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}") """


""" def get_phone(country, area, first, last ):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=123, first=456,last=7890)
print(phone_num)
     """


## 4 . Orbitary argument:
# *args = allows you to pass multiple non key-words

""" def multiply(*args):
    total = 2
    for arg in args:
        total *= arg
    return total

print(multiply(2,3)) """



