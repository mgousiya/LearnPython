#LISTS:

""" students = ["Tahir","Arshad","Mansoor","Ayaan"] """

""" students.append("Tabrez")
print(students) 

new_list = []

for student in students:
    new_list.append(student)
    print(student)
print(new_list) """

#LIST COMPREHENSIONS
""" students = ["Tahir","Arshad","Mansoor","Ayaan"]
students = [student for student in students]
print(students)
 """
# dictionary

bio = {"name":"gousiya",
       "age":26,
       "color":"fair"}

""" print(bio["name"]) """

""" keys = bio.keys()
print(keys) """

""" values = bio.values()
print(values) """

""" cars = [
    {
        "brand" = "Ford"
        "model" = "mustang"
        "year" = "2019"
    }
]

new_list = []
for item in cars:
    new_item = item["brand"]
    new_list.append(new_item)
    print(new_list)
 """
# RANDON

#1. To pick random numbers from given integers we use "RANDINT"
#2. To pick random otems from string we use "CHOICE "
#3.to get float numbers we use random.random() 

import random
""" numbers = random.randint(1,10)
print(numbers) """

""" flowers = ("rose","lilly","marigold","Jasmine")
flowers = random.choice(flowers)
print(flowers) """

""" numbers = random.uniform(0 ,1)
print(numbers) """


# OOPS:

class Cousins:

    def __init__(self,name, age,std):
        self.name =name
        self.age = age
        self.std = std

cousin1 = Cousins("Tahir","15","10")
cousin2 = Cousins("Arshad","12","8")
cousin3 = Cousins("Mannu","9","4")
cousin4 = Cousins("Ayaan","9","4")

print(cousin1.name)
print(cousin3.age)
print(cousin2.std)
print(cousin4.name)