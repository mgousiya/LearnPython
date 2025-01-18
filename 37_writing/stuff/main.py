# Python writing files (.txt, .json, .csv)
""" 
txt_data = "I like Pizza"

file_path = "output.txt"

try:
    with open(file_path, "a")as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("The file already exists") """


#String Example:
""" employees = ["Tahir","Arshad","Mansoor","Ayaan"]

file_path = "output.txt"

try:
    with open(file_path, "w")as file:
       for employee in employees:
        file.write(employee + "\n")
    print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("The file already exists") """

#KEYWORD EXAMPLE:
# dump method will convert the dictionary into json string
""" import json

employee = { 
    "name" : "Tahir",
    "age" : "25",
    "job" : "software"
}

file_path = "output.json"

try:
    with open(file_path, "w")as file:
       json.dump(employee, file, indent = 4)
    print(f"json file '{file_path}' was created")

except FileExistsError:
    print("The file already exists") """

# CSV EXAMPLE

import json
import csv

employees = [["Name","Age","Job"],
             ["Tahir",30,"software"],
             ["Tabrez",25,"umemployeed"],
             ["Arshad",22,"Doctor"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline ="")as file:
       writer = csv.writer(file)
       for row in employees:
           writer.writerow(row)
       print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("The file already exists")