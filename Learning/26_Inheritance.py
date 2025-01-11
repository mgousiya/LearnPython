# Inheritance = Allows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class child(parent)

""" class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

        def eat(self):
            print(f"{self.name} is eating")

        def sleep(self):
            print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("snoofy")
cat = Cat("Snowbell")
mouse = Mouse("Mickey")

print(dog.is_alive) """


# example2

""" class Schools:
    def __init__(self,name):
        self.name = name
       
    def regular(self):
        print(f"The {self.name} student have to come regularly")

    def activity(self):
        print("students need to do activities along with studies")


class Standards(Schools):
    pass

class grades(Schools):
    pass

school = Schools("Arshad")

standard = Standards("8th")
standard.regular() """

#example 3

class Fruits:
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
dryfruit.immune()