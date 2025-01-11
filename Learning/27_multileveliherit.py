# Multiple Inheritance: inherit from more than one parent class.
#                       C(A,B)
# multilevel inheritance: inherit from a parent which inherits from another parent
#                       C(B) <- B(A) <- A

#Example 1:

""" class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


fish.flee()
fish.hunt() """

# Example: 2

""" class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"The {self.name} is eating")
    
    def sleep(self):
        print(f"The {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing")
    
class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.hunt() """