# Prompt the user for their name
guest_name = input("What is your name? ")

# Write the name to the guest.txt file
with open('guest.txt', 'w') as file:
    file.write(guest_name)

print(f"Thank you, {guest_name}, your name has been written to guest.txt.")
