try:
    # Prompt the user for two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert the inputs to integers and add them together
    sum_result = int(num1) + int(num2)

    # Print the result
    print(f"The sum of {num1} and {num2} is: {sum_result}")

except ValueError:
    # Catch the ValueError if either input is not a valid number
    print("Oops! Please enter valid numbers.")
