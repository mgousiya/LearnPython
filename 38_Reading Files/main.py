#Python reading files (.txt, .json, .csv)
# with-statement: The with statement is used to wrap  the execution of a block with 
#                 methods defined by a context manager.
# This allows common try.... except... finally usage patterns to be encapsulated for convinient reuse.


file_path = "C:\Users\HP\Desktop\input.txt"
try:
    with open(file_path, "r") as file:
        content= file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")

