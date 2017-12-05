# Human-guess-machine-number game
"""
Created on Tue Dec  5 23:53:29 2017

@author: Steven

This is the human guess a random-number-generated-by-machine game.
"""

import random

print("HELLO THERE!!\n")
name = input("What is your name? :")

getout = False

while not getout:
    print("\nWell", name, ", I am thinking of a number between 0 to 100.")
    print("You have 10 chances to guess it!")

    number = random.randint(0, 100)
    numGuess = 0
    
    while numGuess < 10:
        numGuess += 1
        
        while True:
            try:                                              #I use the exception handling in this work
                guess = int(input("Take a guess: "))
                if guess < number:
                    print("Your guess is too low.")
                    break
                elif guess > number:
                    print("Your guess is too high.")
                    break
                elif guess == number:
                    break
            except:
                print("Sorry, please enter a number.")
        
        if guess == number:
            print("GOOD JOB", name, "! You guessed my number in", numGuess,"guesses!")
            break
    
    if guess != number:
        print("\nYou have used up 10 chances! The number I was thinking of was", number,".")        
    
    getout2 = False
    while not getout2:
        prompt = input("Another round? (y or n) ")
        if prompt == 'Y' or prompt == 'y':
            break
        elif prompt == 'N' or prompt == 'n':
            print("\nAlright, hope to play with you again soon! Bye!")
            getout2 = True
            getout = True
        else:
            print("Sorry, invalid input")
        
    
        
        