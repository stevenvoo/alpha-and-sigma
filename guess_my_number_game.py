# Machine-guess-your-number Game
"""
Created on Tue Dec  5 22:23:54 2017

@author: Steven

A simple game to test the Bisection algorithm where the MACHINE GUESSES YOUR CHOICE.
"""

print("HELLO THERE!! Are you ready to play a game with me?\n")
print("Let's just say....I CAN PEEK INTO YOUR MIND, GUESS WHAT ARE YOU THINKING hehe\n\n")
print("Shall we?")

getout = False
while not getout:
    print("\nPlease think of a number between 0 - 100\n\n")
    low = 0
    high = 100
    numGuess = 0
    guess = (low + high)//2
    
    while True:
        numGuess += 1
        print("\nIs your secret number", guess, "?")
        choice = input("h - Nope, too high!\n"
                       "l - Nope, too low!\n"
                       "c - Yeah well, you got it.\n"
                       "So? ")
        if choice == 'h' or choice == 'H':
            high = guess
            guess = (low + high)//2
        elif choice == 'l' or choice == 'L':
            low = guess
            guess = (low + high)//2
        elif choice == 'c' or choice == 'C':
            print("I got you! Your secret number is", guess)
            print("Took me", numGuess, "number of guesses.")
            break
        else:
            print("Sorry, invalid input")
    
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
