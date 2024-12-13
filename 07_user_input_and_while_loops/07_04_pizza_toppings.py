# Loop to prompt the user for pizza toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
