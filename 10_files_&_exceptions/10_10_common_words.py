# Ask the user to specify the path to the text file
filename = 'Red_Death.txt'  # Replace with the actual file path

try:
    # Open the file and read its contents
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Count the occurrences of the word 'the' (case insensitive)
    word_count = text.lower().count('the ')
    print(f"The word 'the' appears {word_count} times in the text.")
    
    # Optionally, count the occurrences of 'the' without the space (to count 'then', 'there', etc.)
    general_count = text.lower().count('the')
    print(f"General 'the' count (including words like 'there' and 'then'): {general_count}")

except FileNotFoundError:
    print(f"The file '{filename}' was not found. Please check the file path.")
