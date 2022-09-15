import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances < 5:
    guess = int(input("Enter your number"))
    if guess == number:
        print("Congratulations! You won!")
        break 
    elif guess < number:
        print("Your Guess was too low!")
    else:
        print("Your Guess was too high!")
    chances += 1
if not chances < 5:
    print("You lost! The number is",number)