import requests
import json
from pokemon_class import  Pokemon
base_url: str = 'https://pokeapi.co/api/v2/pokemon/'
def get_pokemon(name: str):
    pokemon = requests.get(f'{base_url}/{name}')
    if pokemon.status_code == 404:
        print('this pokemon cannot be found!')
        return dict()
    return pokemon.json()


def main():
    pokemon_name: str = 'pikachu'
    # pokemon_name: str = 'ditto'
    # pokemon_name: str = 'abra'

    pokemon = get_pokemon(pokemon_name)

    if pokemon:
        # print(json.dumps(pokemon, indent=2))
        print('Pokemon Details')
        p = Pokemon(name=pokemon.get('name'), weight=pokemon.get('weight'), abilities=pokemon.get('abilities'))
        print(f'name: {p.name}'.title())
        print(f'weight: {p.weight}'.title())
        print('abilities'.capitalize())
        for ability in p.abilities:
            print(ability['ability']['name'], 'slots',ability['slot'])




if __name__ == '__main__':
    main()
