# List-Comprehension = A consice to create lists in python 
#                      compact and easier to read than traditional loops
#                      [Expression for valua in iterable if condition ]

# NUMBERS Example

""" doubles = []
for i in range(1, 11):
    doubles.append(i * 2)
print(doubles) """

""" doubles = [i * 2 for i in range(1, 11)]
print(doubles) """

""" triples = [i * 4 for i in range(2,6)]
print(triples) """

""" squares = [i * i for i in range(1,11)]
print(squares) """

## STRING Examples:

""" fruits = ["apple","banana","cherry","orange"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits) """

# returning the first character of each string in the list

""" fruits = ["apple","banana","cherry","orange"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)
 """
# Positive and negitive numbers:

""" numbers = [1,-2,3,-4,-5,6,-7,8]
positive_num = [num for num in numbers if num >= 0]
negitive_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]
print(positive_num)
print(negitive_num)
print(even_num)
print(odd_num) """

# grades example:

grades = [85, 74, 35, 48, 62, 57]
passing_grades =[grade for grade in grades if grade >= 60]
print(passing_grades)
