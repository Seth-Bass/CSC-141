# Create a list of usernames
usernames = []  # You can modify this list to test when it's empty or not

# Check if the list of usernames is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through the list and greet each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
