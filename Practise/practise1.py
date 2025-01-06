# variable example
""" sum = a + b
print(sum) """

# varibale with string

""" email = "gousiya@email.com"
print("email is " + email) """

# variable with f string

""" print(f"my email is {email}") """

# float example
""" age = int(input("Type your age here \n"))
print(f"my age is {age}") """

""" float = float(input())
print(type(float))
 """
# Boolean Example

""" is_iam_in_hyd = True

print(type(is_iam_in_hyd)) """

# Boolean with if else

""" is_hyderabad = False

if is_hyderabad:
    print("Iam in hyd")
else:
    print("Not in hyd") """

# another ex for boolean
""" input  = "Summer"
if input == "Winter" :
    print("Winter")
else:
    print("Summer") """

# If else practise with f string

""" age = int(input("Type your age here \n"))
if age > 30:
    print(f"Go to Balcony beacause your age is {age}")
elif age >= 20 and age <=30:
    print(f"Go to lower Balcony beacause your age is {age}")
elif age > 10 and age <= 20:
    print(f"Go to Normal beacause your age is {age}")
else:
    print(f"Go to regular beacause your age is {age}")  """

# f string example
""" name = input("Type your name here \n")
print(f"my name is {name}") """

# calculator
""" num1 = int(input("Type your num1 here \n"))
num2 = int(input("Type your num2 here \n"))
operator = input("please type your operation + , - , * , % \n")

if operator == "+":
    sum = num1 + num2
    print(sum)
elif operator == "-":
    substract = num1 - num2
    print(substract)
elif operator == "*":
    product = num1 * num2
    print(product)
elif operator == "%":
    quotient == num1 % num2
    print(quotient) """

# example list

""" animals = ["cat","bat","rat","dog"]


animals.append("example")
print(animals)
animals.remove("bat")
print(animals) """

 # Nested List with index
"""flowers = ["rose","Jasmine","lilly"]
food = ["dosa","idly","upma"]
new_list = [flowers,food]
print(new_list[1][2]) """


# for loop
""" flowers = ["rose","Jasmine","lilly"]

for i in flowers:
    for x in i:
        print(x)
    print(i) """


#for loop example -- print each fruit in fruit list

""" fruits = ["orange","papaya","pineapple"]
for i in fruits:
    print(i) """

# for loop -- loop through letters in the word
""" 
for x in "papaya":
    print(x) """

# forloop --break statement--if print statement is given first before the condition it will take the given break value

""" fruits = ["orange","papaya","pineapple"]
for i in fruits:
    print(i)
    if i == "papaya":
      break
"""

# forloop-- break statement--if condition is given first and then break statement it will end before the break value

""" fruits = ["orange","papaya","pineapple"]
for i in fruits:
    if i == "papaya":
       break
    print(i) """

# forloop --continue -- it will break the loop of given iteration and continue with the next

""" fruits = ["orange","papaya","pineapple"]
for i in fruits:
    if i == "papaya":
       continue
    print(i)
 """
# Nested loops -- 

""" wages = ["test","best","worst"]
matches = ["cricket","football"]
for i in wages:
    for x in matches:
        for y in x:
            print(y)
        print(x)
print(i) """

# Nested loops example ---

""" 
adj = ["green", "leafy", "juicy"]

vegetables = ["spinach", "kale", "pumpkin"]

for x in adj:
   for y in vegetables:
        for z in y:
            print(z)
        print(x,y)
    """

# while loop --- star format

""" n = int(input("Type your number here \n"))
counter = 0
while counter < n:
    print("* " * n)
    counter = counter + 1
 """

""" 
i = 1
while i < 6:
    print(i)
    i += 1 """

# while loop -- break statement
""" i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1 """

# While loop -- continue statement
""" i = 0
while i < 6:
    i += 1
    if (i == 3):
        continue
    print(i) """

# while loop using --- Else statement
""" i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6") """



# Dictionary

""" fruits = {
    "student1": "eliyaz",
    "student2": "gouisya",
    "student3": "arshad"    
}

for value in fruits.values():
    print(value) """



""" fruits = ["apple","melom","grapes"]

new_list = []

score = 0
for fruit in fruits:
    new_list.append(fruit)
    print(fruit)
    score +=  1

print(new_list)
print(score)

 """




""" import random

ans = random.randint(1,100)
print(ans) """