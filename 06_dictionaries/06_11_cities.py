# Creating a dictionary called cities with information about each city
cities = {
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Paris is known as the City of Light.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is one of the most populous cities in the world.'
    },
    'New York': {
        'country': 'United States',
        'population': 8419600,
        'fact': 'New York is famous for the Statue of Liberty and Central Park.'
    }
}

# Looping through the dictionary and printing the information about each city
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
