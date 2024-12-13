try:
    # Try to read the contents of cats.txt
    with open('cats.txt', 'r') as cats_file:
        cats = cats_file.readlines()
    print("Cat names:")
    for cat in cats:
        print(cat.strip())  # Strip removes the newline character at the end of each line
    
    # Try to read the contents of dogs.txt
    with open('dogs.txt', 'r') as dogs_file:
        dogs = dogs_file.readlines()
    print("\nDog names:")
    for dog in dogs:
        print(dog.strip())  # Strip removes the newline character at the end of each line

except FileNotFoundError as e:
    print(f"Error: {e}. One or both of the files are missing.")
