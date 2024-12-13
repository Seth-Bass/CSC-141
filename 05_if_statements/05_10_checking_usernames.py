# List of current usernames
current_users = ['alice', 'bob', 'charlie', 'admin', 'jane']

# List of new usernames to check
new_users = ['david', 'admin', 'john', 'Alice', 'bob']

# Make a copy of current_users with all usernames in lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through the new users and check if the username is already taken
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")
