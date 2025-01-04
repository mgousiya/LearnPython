import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
""" 
dice = []
total = 0
user_input = int(input("please roll the die with side in range(1,6): \n"))

for die in range(user_input):
    dice.append(random.randint(1,6))

print(dice)

for die in dice:
    total += die

print(total) """ 


dice = []
total = 0
user_input = int(input("Please select your num in range(1,6) \n"))

for die in range(user_input):
    dice.append(random.randint(1,6))
print(dice)

for sum in dice:
    total += sum

print(total)

 
