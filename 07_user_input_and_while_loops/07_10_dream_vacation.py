# Create an empty list to store the vacation destinations
vacation_destinations = []

# Poll users for their dream vacation destination
print("If you could visit one place in the world, where would you go?")
print("Enter 'quit' to end the poll.\n")

# Loop to continuously ask for input until 'quit' is entered
while True:
    destination = input("Where would you go? ")

    if destination.lower() == 'quit':
        break
    else:
        vacation_destinations.append(destination)

# Print the results of the poll
print("\n--- Poll Results ---")
for i, destination in enumerate(vacation_destinations, 1):
    print(f"{i}. {destination}")
