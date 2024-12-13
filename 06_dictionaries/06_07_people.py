# Dictionaries representing information about three different people
person_1 = {
    'first_name': 'Luke',
    'last_name': 'Skywalker',
    'age': 30,
    'city': 'New York'
}

person_2 = {
    'first_name': 'Han',
    'last_name': 'Solo',
    'age': 25,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Boba',
    'last_name': 'Fett',
    'age': 35,
    'city': 'Chicago'
}

# List to store all three dictionaries
people = [person_1, person_2, person_3]

# Loop through the list of people and print everything about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
