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

book1 = Book("Gitanjali","Rabindranath Tagore",365)
book2 = Book("The wings of fire","Dr. APJ",320)
book3 = Book("Wise and Otherwise","Sudha Murthy",280)

print(book1 < book2)