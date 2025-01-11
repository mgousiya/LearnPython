# Super() = Function used in a child class to call methods from a parent class(super class)
#           Allows to extend the functionality of the inherit methods


""" class Circle:
    def __init__(self,color,filled,radius):
        self.color = color
        self.filled = filled
        self.radius = radius

class Square:
    def __init__(self,color,filled,width):
        self.color = color
        self.filled = filled
        self.width = width

class Triangle:
    def __init__(self,color,filled,width,height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height """
# what if i want to change the filled to is_filled manually it will miss in some places so 
# by using super() we will write the code

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}") 


class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height


square = Square("blue",True, 6)

print(square.width)