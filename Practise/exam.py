""" # range example
for i in range(0,100):
    print(i)
    
    

# range with step
for i in range(0,50,5):
    print(i)
 """

""" flowers = ["lilly","rose","jasmine","marigold"]
f1 = []
f2 = []
f3 = []
f4 = []

for flower in flowers:
    f1.append(flowers[0])
    f2.append(flowers[1])
    f3.append(flowers[2])
    f4.append(flowers[3])
print(f1,f2,f3,f4) """

# range using step
""" for i in range(0,100,5):
    print(i) """

# dictionary --- Nested loop dictionary

biodata = {"name":"gousiya",
           "rollno":"22"}
        
""" education = {"education":"BSC",
             "group":"CSC"} """

""" new_biodata = {"a":biodata["name"],"b":education["group"]}
print(new_biodata) """

""" for key,value in biodata.items():
    print(f"{key},{value}") """
    
## Slot machine
""" 
# Python slot machine
import random

def spin_row():
    Symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(Symbols) for _ in range(3)]

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100

    print("***********************")
    print("Welcome to Python slots")
    print("Symbols : 🍒 🍉🍋🔔⭐")
    print("***********************")

    while balance > 0:
        print(f"current balance is ${balance}")

        bet = input("Please enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue
        if bet <= 0:
            print("Bet should be greater than 0")
            continue 

        balance =- bet

        row = spin_row
        print(row) """







""" 
if __name__ == "__main__":
    main() """


""" animals = ["cat","dog","rat"]
new_animals = [] """

""" class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def lecture():
        print("The children are playing")

children = Students("Tahir",14,"A")

print(children.name)

Students.lecture()
 """

#Example:

""" class Fruits:
    def __init__(self,name):
        self.name = name

    def healthy(self):
        print(f"{self.name} is a healthy ")

    def immune(self):
        print(f"{self.name} is a healthy ")

    def habit(self):
        print(f"Consuming {self.name} is good for body")

class Vegetables(Fruits):
    pass

class Dryfruits(Fruits):
    pass

sample = Fruits("Orange")
print(sample.name)

vegetable = Vegetables("Tomato")
dryfruit = Dryfruits("Almond")

vegetable.immune()
dryfruit.immune() """