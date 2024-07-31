import random

top_of_range = input("Please enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit() 
else:
    print("Please type a number next time.")
    quit() 

random_number = random.randint(0, top_of_range)
guesses = 0 

while True:
    guess = input("Please enter your guess: ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if guess == random_number:
            print("Correct!")
            break 
        elif guess > random_number:
            print("Too high")
        else:
            print("Too low")
print("It took you " + str(guesses) + " guesses")