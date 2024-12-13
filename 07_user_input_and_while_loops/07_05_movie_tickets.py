# Loop to ask for user's age and tell them the cost of the movie ticket
while True:
    age = input("Please enter your age (or type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break
    
    # Convert the age to an integer
    age = int(age)
    
    # Determine the ticket price based on age
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"The cost of your movie ticket is ${price}.")
