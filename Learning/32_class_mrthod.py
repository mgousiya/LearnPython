# Class Methods = Allow operations related to the class itself
#               Take (cls) as the first parameter, which represents the class itself

#Instance Methods = Best for operations on instances of the class (objects)
#Static Method = Best for utility functions that do not need access to class data
#Class Method = Best for class level data or requires access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name}{self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
            
    


student1 = Student("Tahir",4.1)
student2 = Student("Arshad",4.0)
student3 = Student("Mansoor",4.3)
student4 = Student("Ayaan",4.5) 

print(Student.get_count())
print(Student.get_avg_gpa())