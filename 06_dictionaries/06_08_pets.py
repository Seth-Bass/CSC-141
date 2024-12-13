# Dictionaries representing information about different pets
pet_1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'cat',
    'owner': 'Bob'
}

pet_3 = {
    'animal': 'parrot',
    'owner': 'Charlie'
}

pet_4 = {
    'animal': 'hamster',
    'owner': 'Diana'
}

# List to store all the pet dictionaries
pets = [pet_1, pet_2, pet_3, pet_4]

# Loop through the list of pets and print everything about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")
