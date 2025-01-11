# Static Method = A method that belongs to a class rather than any object from
#                that class(instance)
# ------------- Usually used for general utility functions

#Instance Methods = Best for oprations on instances of the class(objects)
# Static Method = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions

employee1 = Employee("Edward","Manager")
employee2 = Employee("Einstien","Cashier")
employee3 = Employee("Tony","Cook")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())