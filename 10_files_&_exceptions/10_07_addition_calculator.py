while True:
    try:
        # Prompt the user for two numbers
        num1 = input("Enter the first number (or 'quit' to exit): ")
        if num1.lower() == 'quit':  # Allow user to quit the loop by typing 'quit'
            print("Goodbye!")
            break
        
        num2 = input("Enter the second number: ")
        if num2.lower() == 'quit':  # Allow user to quit the loop by typing 'quit'
            print("Goodbye!")
            break

        # Convert the inputs to integers and add them together
        sum_result = int(num1) + int(num2)

        # Print the result
        print(f"The sum of {num1} and {num2} is: {sum_result}")
    
    except ValueError:
        # Catch the ValueError if either input is not a valid number
        print("Oops! Please enter valid numbers.")
