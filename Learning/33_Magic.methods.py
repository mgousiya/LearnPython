# Magic methods = Dunder Methods(double underscore)__init__,__str__,__eq__
#                They are automatically called by many of the python's built in operators.
#                They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author= author
        self.num_pages = num_pages  

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__ (self,other):
        return self.title == other.title and self.author == other.author 
    
    def __lt__(self,other):
        return self.num_pages < other.num_Pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author

book1 = Book("Gitanjali","Rabindranath Tagore",365)
book2 = Book("The wings of fire","Dr. APJ",320)
book3 = Book("Wise and Otherwise","Sudha Murthy",280)


print(book2['author'])





#1. __init__(self): Initilizer method(constructor) for creating an instance of a class.
#2.__str__(self): defines the string representation of an object when using str() or print()
#3.__eq__(self,other): Allows comparison between two objects using == operator
#4.__lt__(self,other): (<) less than operator between two objects
#5.__gt__(self,other):(>)greater than operator between two objects
#6.__add__(self,other): (+) operator to add two objects
#7.__len__(self): behaviour of len() when called an object
#8.__getitem__(self,key): allows the use of square brackets[] to access elements of an object,
#                        as with list or dictionaries.
#9.__setitem__(self,key,value): defines behaviour when assigning values to an object using
#                             square brackets.[]
#10.__contains__: To find the particular word 
