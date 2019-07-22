import random

#this is the guess game
name = input("Enter your name :: ")
print("well " + name + " i m guessing a number between 1 and 20")
secret_number = random.randint(1, 20)

#ask the player to guess 6 times
def guess_loop(range_):
    for i in range(range_):
        guessed_number = int(input("take a guess :: "))
        if guessed_number > secret_number:
            print("guessed number is high")
        elif guessed_number < secret_number:
            print("guessed number is low")
        else:
            return guessed_number

guessed_number = guess_loop(6)

if guessed_number == secret_number:
    print("Good Job, " + name + " number is " + str(secret_number))
else:
    print("Oops failed, number is " + str(secret_number))
