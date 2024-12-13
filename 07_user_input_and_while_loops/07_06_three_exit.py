# Version 1: Using a conditional test in the while statement to stop the loop
topping = ''
while topping != 'quit':  # The loop will stop when the user types 'quit'
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")
    
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

# Version 2: Using an active variable to control how long the loop runs
active = True
while active:
    age = input("Please enter your age (or type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        active = False  # Stop the loop if 'quit' is entered
    else:
        # Convert the age to an integer and determine the ticket price
        age = int(age)
        
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        
        print(f"The cost of your movie ticket is ${price}.")

# Version 3: Using a break statement to exit the loop when the user enters 'quit'
while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")
    
    if topping == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    print(f"I'll add {topping} to your pizza.")
