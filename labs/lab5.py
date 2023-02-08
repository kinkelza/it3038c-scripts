# Write a 'guess the number game' where a random number is generated and the user must guess the number. The program says if their number is too high or too low until the right answer is guessed.

import random #get random class

num = int(random.randint(1, 100)) #set a random int between 1 and 100

# print(num) # for testing lets you know the num to verify its working

while (True):
    print("Please guess a number between 1 and 100")
    numguess = int(input())
    if numguess == num:
        print("You Guessed the number")
        break;
    elif numguess > num:
        print("Your guess was to high, guess a lower number")
    elif numguess < num:
        print("Your guess was to low, guess a higher number")
    else:
        pint("An error has occured please retry the program")
        break;

print("Thanks for playing, please come again")
