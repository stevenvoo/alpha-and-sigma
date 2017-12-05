# Testing Cube root calculator (Bisection method)
"""
Created on Sun Dec  3 22:41:16 2017

@author: Steven

I do this to test my thinking in numerical algorithm, and of course
you can use math library to calculate cube root much much simpler heh.
"""

#For cube root more than 1
def cuberoot2(cube):
    numGuess = 0
    epsilon = 0.01
    low = 1
    high = cube
    guess = (low + high)/2

    while abs(cube - guess**3) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high)/2
        numGuess += 1

    print("number of iteration =", numGuess)
    print(guess, "is close to the cube root of", cube)
    return numGuess and guess and cube

#For cube root of 0 to 1
def cuberoot1(cube):
    numGuess = 0
    epsilon = 0.00001
    low = cube
    high = 1
    guess = (low + high)/2

    while abs(cube - guess**3) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high)/2
        numGuess += 1

    print("number of iteration =", numGuess)
    print(guess, "is close to the cube root of", cube)
    return numGuess and guess and cube

#For cube root less than -1
def cuberootneg2(cube):
    numGuess = 0
    epsilon = 0.01
    low = cube
    high = -1
    guess = (low + high)/2

    while abs(cube - guess**3) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high)/2
        numGuess += 1

    print("number of iteration = ", numGuess)
    print(guess, "is close to the cube root of", cube)
    return numGuess and guess and cube

#For cube root from -1 to 0
def cuberootneg1(cube):
    numGuess = 0
    epsilon = 0.00001
    low = -1
    high = cube
    guess = (low + high)/2

    while abs(cube - guess**3) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high)/2
        numGuess += 1

    print("number of iteration =", numGuess)
    print(guess, "is close to the cube root of", cube)
    return numGuess and guess and cube


getout = False
print("Hello there, this is a super cube root calculator.")

while not getout:
    cube = float(input("Enter your number: "))
    if cube >= 1:
        cuberoot2(cube)
    elif cube > 0 and cube < 1:
        cuberoot1(cube)
    elif cube <= -1:
        cuberootneg2(cube)
    else:
        cuberootneg1(cube)

    getout2 = False
    while not getout2:
        prompt = input("Continue? (y or n): ")
        if prompt == 'N' or prompt == 'n':
            print("Thank you and have a nice day.")
            getout2 = True
            getout = True
        elif prompt == 'Y' or prompt == 'y':
            getout2 = True
            getout = False
        else:
            print("Sorry, invalid input.")
           
    


