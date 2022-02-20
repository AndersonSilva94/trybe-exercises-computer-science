import json

with open("pokemons.json") as file:
    # content = file.read()
    # pokemons = json.loads(content)["results"]
    pokemons = json.load(file)["results"]

# print(pokemons[0])

grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

with open("grass_pokemons.json", "w") as file:
#    json_to_write = json.dumps(
#        grass_type_pokemons
#    )
    json.dump(grass_type_pokemons, file)
