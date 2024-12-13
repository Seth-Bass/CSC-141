# Dictionary storing programming terms and their meanings
glossary = {
    'variable': 'A variable is a reserved memory location to store values.',
    'loop': 'A loop is a control structure that repeats a block of code multiple times.',
    'function': 'A function is a block of code that only runs when it is called.',
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary is a collection of key-value pairs where each key is unique.'
}

# Printing each word and its meaning in a formatted way
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n{meaning}\n")