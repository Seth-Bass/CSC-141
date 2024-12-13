# Open the file in append mode ('a') so that new names are added to the file without overwriting
with open('guest_book.txt', 'a') as file:
    while True:
        # Prompt the user for their name
        guest_name = input("What is your name? (Type 'quit' to stop) ")
        
        # Check if the user wants to exit the loop
        if guest_name.lower() == 'quit':
            break
        
        # Write the name to the guest_book.txt file, each on a new line
        file.write(guest_name + "\n")

print("Thank you for signing the guest book!")