# Extended cities dictionary with more details
cities = {
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Paris is known as the City of Light.',
        'famous_landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
        'currency': 'Euro',
        'language': 'French'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is one of the most populous cities in the world.',
        'famous_landmarks': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing'],
        'currency': 'Yen',
        'language': 'Japanese'
    },
    'New York': {
        'country': 'United States',
        'population': 8419600,
        'fact': 'New York is famous for the Statue of Liberty and Central Park.',
        'famous_landmarks': ['Statue of Liberty', 'Empire State Building', 'Central Park'],
        'currency': 'US Dollar',
        'language': 'English'
    }
}

# Loop through the dictionary and print extended details about each city
for city, info in cities.items():
    print(f"\n--- {city} ---")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print(f"Famous Landmarks: {', '.join(info['famous_landmarks'])}")
    print(f"Currency: {info['currency']}")
    print(f"Language: {info['language']}")
    print("-" * 30)
