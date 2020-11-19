# Modify number gusessing number
# Guess a number

import random
winning_number = 43
guess = 1
game_over = False

while True:
    number = int(input("guess a number between 1 and 100 : "))
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times ")
        break
    else:
        if number < winning_number:
            print("too low ")
        else:
            print("too high")

        guess += 1
        continue
# DRY - don't repeat yourself
