# Dictionary of people who have already responded to the poll and their favorite languages
favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'c++',
    'diana': 'ruby'
}

# List of people who should take the poll
polling_people = ['alice', 'bob', 'eve', 'frank', 'charlie', 'george']

# Loop through the list of people who should take the poll
for person in polling_people:
    if person in favorite_languages:
        print(f"Thank you for responding, {person.title()}!\n")
    else:
        print(f"Hi {person.title()}, we would like to invite you to take the poll!\n")
