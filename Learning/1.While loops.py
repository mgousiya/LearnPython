# while loop = execute some code WHILE some condition remains TRUE

 ## Name Example ----
""" name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
    print(f"Hello {name}")
 """
 ## Age Example -----
 
""" age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
    print(f"you are {age} years old")
"""

## Food Example ___ (using "not true" here)
food = input("Enter your favourite food (q to quit): ")
while not food == "q":
    print(f"your favourite is {food}")
    food = input("Enter your another favourite food (q to quit): ")
print("Bye")
 

## Number Example --- using "or operator "

""" num = int(input("Select a num between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Select a num between 1-10: "))
print(f"your num is {num}") """