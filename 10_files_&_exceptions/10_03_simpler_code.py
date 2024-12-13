# Open the file and print each line after splitting into lines
with open('learning_python.txt', 'r') as file:
    for line in file.read().splitlines():
        print(line)
