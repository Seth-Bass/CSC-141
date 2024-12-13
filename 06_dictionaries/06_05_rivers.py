# Dictionary storing rivers and the countries they flow through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.\n")

# Loop to print the name of each river
print("Rivers in the dictionary:")
for river in rivers:
    print(river.capitalize())

# Loop to print the name of each country
print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country.capitalize())
