# Open the file and read the entire contents at once
with open('learning_python.txt', 'r') as file:
    content = file.read()  # Read the entire file
    print("Contents read all at once:")
    print(content)

# Open the file and read it line by line, storing the lines in a list
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()  # Read the file into a list of lines
    print("\nContents read line by line:")
    for line in lines:
        print(line.strip())  # Use .strip() to remove extra newline characters
