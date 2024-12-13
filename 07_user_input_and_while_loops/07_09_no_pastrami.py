# List of sandwich orders
sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'cheese', 'pastrami', 'veggie']

# Empty list to store finished sandwiches
finished_sandwiches = []

# Print a message indicating the deli is out of pastrami
print("The deli has run out of pastrami!\n")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining sandwich orders
while sandwich_orders:
    # Take an order from the sandwich_orders list
    current_sandwich = sandwich_orders.pop()

    # Print the message about the sandwich
    print(f"I made your {current_sandwich} sandwich.")

    # Add the finished sandwich to the finished_sandwiches list
    finished_sandwiches.append(current_sandwich)

# After all sandwiches are made, print out the list of finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
