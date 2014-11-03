# Import random number generator
import random

keepplaying = True
my_number = 0
guess = 0
quitvariable = " "



while keepplaying == True:
    
    my_number = random.randrange(1,101)
    
    print()
    print("Guess the random number between 1 and 100")
    print()
    guess = int(input("Guess the number: "))
    
    while guess != my_number:
        
        if guess > my_number:
            print("Too high.")
            print()
            guess = int(input("Guess the number: "))
            print()
            
        elif guess < my_number:
            print("Too low.")
            print()
            guess = int(input("Guess the number: "))
            print()
            
    else:
        print("You won! Good Job!")
        print()
        quitvariable = input("Play again? Y or N?")    
        
        if str.lower(quitvariable) == "y":
            keepplaying = True
        else:
            print("Ok, don't play my game :(")
            keepplaying = False

print("Bye!")
