class School:
    def __init__(self,name,place,grade):
        self.name = name
        self.place = place
        self.grade = grade

    def essentials(self):
        print("That is a very famous and old school")

example = School("Santiniketan","PKD","A+")

print(example.name)
example.essentials()
