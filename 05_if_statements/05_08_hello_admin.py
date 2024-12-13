# Create a list of usernames, including 'admin'
usernames = ['alice', 'bob', 'admin', 'jane', 'charlie']

# Loop through the list and greet each user
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
