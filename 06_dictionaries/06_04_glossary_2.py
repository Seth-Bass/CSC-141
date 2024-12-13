# Extended dictionary storing programming terms and their meanings
glossary = {
    'variable': 'A variable is a reserved memory location to store values.',
    'loop': 'A loop is a control structure that repeats a block of code multiple times.',
    'function': 'A function is a block of code that only runs when it is called.',
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary is a collection of key-value pairs where each key is unique.',
    'tuple': 'A tuple is an immutable collection of items in a specific order.',
    'class': 'A class is a blueprint for creating objects in object-oriented programming.',
    'method': 'A method is a function that is associated with an object and is part of a class.',
    'inheritance': 'Inheritance is a mechanism in object-oriented programming where a class can inherit properties and methods from another class.',
    'boolean': 'A boolean is a data type that can have one of two values: True or False.'
}

# Looping through the dictionary and printing each key-value pair
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n{meaning}\n")
