
# Sets the number of numbers to take the mean of
quantity = int(input("How many numbers do you want to average?"))

# Error checking. You have to average at least one number
if quantity > 0:
   
    # Sets the initial average to zero.
    # Input here so first instance shows as "First"
    average = 0
    
    first_number = float(input("Enter your first number: "))
    average = first_number
    
    # Separate section so the first instance asks for "first"
    if quantity == 1:
        
        print("The average is {:.2f}".format(average))
    
    # Loops through quantities of numbers larger than 0
    elif quantity > 1:
        
        for i in range(quantity - 1):
            current_number = float(input("Enter your next number: "))
            average = average + current_number
            
        average = average / quantity
        
        print("The average is {:.2f}".format(average))

# Handles all instances where user enters 0 or negative number of numbers.
else:
    
    print("You can't average no numbers or a negative number of numbers")
