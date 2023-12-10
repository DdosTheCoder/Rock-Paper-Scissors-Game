import random

user_wins = 0
python_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q".lower():
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    python_pick = options[random_number]
    print("Python chose:",python_pick)

    if user_input == "rock" and python_pick == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and python_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == "scissors" and python_pick == "paper":
        print("You won")
        user_wins += 1

    else:
        print("You lost!")
        python_wins += 1

print("You won: {} times | python won: {} times".format(user_wins,python_wins))

print("Goodbye")