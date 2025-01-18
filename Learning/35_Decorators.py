# DECORATOR: A function that extends the behaviour of another function
#            without modifying main function
#            pass the base function as argument to the decorator
#             

def add_sprinkels(func):
    def wrapper(*args,**kwargs):
        print("*You add sprinkle🎊*")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("*You add a fudge🍫*")
        func(*args,**kwargs)
    return wrapper


@add_sprinkels
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍨")

get_ice_cream("Chocolate")