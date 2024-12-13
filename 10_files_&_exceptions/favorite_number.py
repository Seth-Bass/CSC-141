import json

# Prompt the user for their favorite number
favorite_number = input("What's your favorite number? ")

# Convert the input to an integer (if needed, can handle other types here)
favorite_number = int(favorite_number)

# Store the favorite number in a file using json.dumps()
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print(f"Your favorite number {favorite_number} has been saved.")
