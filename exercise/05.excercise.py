# Exercise, NUMBER Guessing Game
# Make a variable, like winning_number and assign any NUMBER to it.
# Ask user to guess a NUMBER
# if user guessed correctly then print "You Win !!!"
# if user didn't guessed lower then actual number then print "too low"
# if user didn't guessed high then actual number then print "too high"

# google "how to generate random number in python " to generate random
# winning_number

number = 25
guess = int(input("Guess a Number 1 to 50 : "))

if number > guess:
    print("too low")
elif number < guess:
    print("too high")
else:
    print("YOU WIN !!!!!") 