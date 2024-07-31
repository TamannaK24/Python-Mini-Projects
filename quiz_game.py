print("Welcome to the quiz game!")
playing = input("Do you want to play? (yes or no)? ") 

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What is a cpu? ").lower()
if answer != "central processing unit":
    print("Incorrect!")
else:
    print("Correct!")
    score+=1

answer = input("What is a gpu? ").lower()
if answer != "graphics processing unit":
    print("Incorrect!")
else:
    print("Correct!")
    score+=1

answer = input("What is a ram? ").lower()
if answer != "random access memory":
    print("Incorrect!")
else:
    print("Correct!")
    score+=1

answer = input("What is a psu? ").lower()
if answer != "power supply":
    print("Incorrect!")
else:
    print("Correct!")
    score+=1

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.") 