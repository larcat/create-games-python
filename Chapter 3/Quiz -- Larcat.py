print("This is a quiz you have to take.")

# Setting up initial variables
current_answer = ""
number_correct = 0
name = " "

# Question 1
print("Question 1:")
name = input("What is your name? ")
print()
print("Hi {!r}, good job getting the first question right!".format(name))
number_correct += 1
print()

# Question 2
print("What is the President's name?")
print()
print("A) RONALD REAGAN")
print("B) JIMMY BUTLER")
print("C) WOODY WOODPECKER")
print("D) BARACK OBAMA")
print()
current_answer = input("Your answer: ")
print()

#Checks for rightness of question 2
if current_answer == "D" or current_answer == "d":
    print("You got it right! OB is pres!")
    number_correct += 1
    print()
    
else:
    print("So sad. Wrong :\(")
    print()
    
# Question 3
current_answer = input("What is 2 + 2? ")
print()

#Checks for rightness of question 3
if str.lower(current_answer) == "four" or int(current_answer) == 4:
    print("You got it right! Four is correct!")
    number_correct += 1
    print()
    
else:
    print("So sad. Wrong :\(")
    print()

# Question 4
print("Bebe is ferocious. True or False? ")
print()
print("A) True")
print("B) False")
print()
current_answer = input("Your answer: ")
print()

#Checks for rightness of question 4
if str.lower(current_answer) == "a":
    print("You got it right! Bebe IS ferocious.")
    number_correct += 1
    print()
    
else:
    print("So sad. Wrong Everyone knows Bebe is ferocious :\(")
    print()

# Question 5
print("Sinner is dorky. True or False? ")
print()
print("A) True")
print("B) False")
print()
current_answer = input("Your answer: ")
print()

#Checks for rightness of question 5
if str.lower(current_answer) == "a":
    print("You got it right! Sinner IS dorky.")
    number_correct += 1
    print()
    
else:
    print("So sad. Wrong Everyone knows Sinner is dorky :\(")
    print()

print("Quiz complete! Computing score.")
print()

print(20 * number_correct, "% Correct.")
