# List of sandwich orders
sandwich_orders = ['tuna', 'ham', 'turkey', 'cheese', 'veggie']

# Empty list to store finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders and process each one
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
