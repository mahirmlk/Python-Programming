"""
API calls fetch data from the internet.
Using Pokemon API: https://pokeapi.co/
"""

import requests

# Get a single Pokemon
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

print(f"Name: {data['name']}")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")

# Get Pokemon abilities
print("\nAbilities:")
for ability in data['abilities']:
    print(f"- {ability['ability']['name']}")

# Get Pokemon types
print("\nTypes:")
for ptype in data['types']:
    print(f"- {ptype['type']['name']}")

# Function to get Pokemon info
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [t['type']['name'] for t in data['types']]
        }
    else:
        return None
