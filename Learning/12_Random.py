import random
# print(help(random))
""" number = random.randint(1,6)
print(number) """

# we can give values using variable in range
""" low = 1
high = 100
number = random.randint(low,high)
print(number)
 """
# to get float numbers we use random.random() method

""" number = random.random()
print(number) """

# choice method is used to pick the random options(string)

""" options =("rock","paper","scissors") 
option = random.choice(options)
print(option) """



## number guess program

""" game_continue = True
game_lives = 5
computer_input = random.randint(0,10)

print(computer_input)
while game_continue:
    user_input = int(input("type your guessing number: \n"))
    if computer_input == user_input:
        print(f"You Won, because computer choose the number {computer_input}")
        do_you_want_to_continue_game = input("please type yes for continue or type quit \n")
        if do_you_want_to_continue_game == "yes".lower():
            pass
        elif do_you_want_to_continue_game == "quit".lower():
            break

    else:
        print(f"You Loss, because computer choose the number {computer_input}")
        game_lives -= 1
        print(f"games lives {game_lives}")
        if game_lives <= 0:
            game_continue = False
            print("you're lives are over.Try again")
         """

""" computer_num = random.randint(0,5)
game_continuation = True
user_live = 3
while game_continuation:
    user_input = int(input("Type your guess number here \n"))
    if computer_num == user_input:
        print(f"You won, computer num is also {computer_num}")
        user_want_to_continue = input("Type yes to continue or q to quit \n").lower()
        if user_want_to_continue == "yes":
            pass
        elif user_want_to_continue == "q":
            break
    else:
        print(f"You loss, computer selected num is {computer_num}")
        user_live -= 1
        if user_live == 0:
            print(f"user_live are {user_live}")
            game_continuation = False
            print("Game exited because you loss lives")

 """

## Rock, paper, scissor game:

""" import random
options = ("Rock","paper","scissor")
computer_choice = random.choice(options)
game_continue = True
score = 0

while game_continue:
    user_choice = input(f"Please select from{options}\n").lower()
    if user_choice == computer_choice:
        print("Game Tie")
    elif user_choice == "Rock" and computer_choice == "scissor":
        print("you Won, because Rock will break scissor")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("you Won, because paper will cover the Rock")
    elif user_choice == "Scissor" and computer_choice == "paper":
        print("you Won because scissor cut the paper")
    else:
        print("you loose")
        score += 1
        if score > 5:
            game_continue = False """






