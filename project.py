import requests

pokemon = input("Enter you favorite pokemon NAME! ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)

data = req.json()

print(f"The choosed pokemon NAME is {data['name']}")
print("And this pokemon have abilities of : ")
for ability in data['abilities']:
    print(ability['ability']['name'])