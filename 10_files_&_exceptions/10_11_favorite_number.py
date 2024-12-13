import json

# Load the favorite number from the file
filename = 'favorite_number.json'
try:
    with open(filename, 'r') as f:
        favorite_number = json.load(f)
    print(f"I know your favorite number! It’s {favorite_number}.")
except FileNotFoundError:
    print("The file containing your favorite number is not found.")
