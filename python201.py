# Import essential packages
import requests

# Ask user input 
pokemon = input("Choose your pokemon: ").lower()

# Create a dynamic URL based on step 1
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

# Fetch the data from the Url in step 2
req = requests.get(url)

# If Pokemon does not exist, use the if condition to prevent errors!
if req.status_code == 200:
    # Convert JSON to a dictionary and print out pokemon data
    data = req.json()
    print(f"Name is\t\t{data['name']}\nAbilities:")
    abi = [print(ability['ability']['name']) for ability in data['abilities']]

else:
    # Print the following message if an error occurs.
    print("Pokemon not found")