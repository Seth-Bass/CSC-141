# Open the file and read each line
with open('learning_python.txt', 'r') as file:
    for line in file:
        modified_line = line.replace('Python', 'C')  # Replace 'Python' with 'C'
        print(modified_line.strip())  # Print the modified line, stripping any leading/trailing whitespace
