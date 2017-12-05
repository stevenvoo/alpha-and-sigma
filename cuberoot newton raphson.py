#Testing Cube root calculator (Newton-Raphson method)
"""
Created on Tue Dec  5 22:02:28 2017

@author: Steven

I use Newton-Raphson method to calculate the problem, obviously the convergence
rate of Newton-Raphson is much faster than Bisection, and the algorithm is simpler
and shorter. What's more, we can solve more polynomial functions with 
Newton-Raphson method. 
"""

print("Hello there, this is a super cube root calculator.")

getout = False

while not getout:
    numGuess = 0
    epsilon = 0.00001
    cube = float(input("Enter number: "))
    if cube < -1 and cube > 1:             
        guess = cube / 10                 #You can start with any guess, I put it this way
    else:                                 # so that the iteration converge faster.  
        guess = cube

    while abs(cube - guess**3) >= epsilon:
        guess = guess - ((guess**3 - cube)/(3 * guess**2))
        numGuess += 1

    print("number of iteration = ", numGuess)
    print(guess, "is close to the cube root of ", cube)
    
    getout2 = False
    while not getout2:
        prompt = input("Continue? (y or n): ")
        if prompt == 'N' or prompt == 'n':
            print("Thank you and have a nice day.")
            getout2 = True
            getout = True
        elif prompt == 'Y' or prompt == 'y':
            getout2 = True
        else:
            print("Sorry, invalid input.")
