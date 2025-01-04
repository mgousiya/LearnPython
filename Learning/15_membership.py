# membership operators: uses to test a value or variable is found in a sequence
#                     (string, list, tuple, dictionary)
#                      1. in 2. not in

""" fruits = {"apple","grape","orange"}
print("apple" not in fruits)

print("papaya" in fruits) """


game_on = True
word = "APPLE"

while game_on:
    letter = input("type the input here \n")
    if letter in word:
        print(f"There is the {letter} in {word}")
        game_continue = input("type yes for continue or Q for Quit \n")
        if game_continue == "yes".lower():
            pass
        elif game_continue == "q".lower():
            break
    else:
        print(f"There is no {letter} in {word}")
        game_continue = input("type yes for continue or Q for Quit \n")
        if game_continue == "yes".lower():
            pass
        elif game_continue == "q".lower():
            break

