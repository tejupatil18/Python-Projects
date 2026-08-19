guess = int(input("Guess a number between 1 to 100 :"))
from ast import While
import random as rand
random_number = rand.randint(1, 100)
count = 1

while True :
    if guess == random_number:
        print("You guessed the correct number")
        break
    else:
        if guess < random_number:
            
            print("You guessed the wrong number. The correct number is greater than your guess")
        else:
            print("You guessed the wrong number. The correct number is less than your guess")

        guess = int(input("Guess again: "))
        count += 1


print("You guessed the correct number in", count, "attempts")