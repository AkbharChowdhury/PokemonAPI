import pprint
from typing import Any
from pprint import pprint
import requests
import json
from pokemon_class import Pokemon

base_url: str = 'https://pokeapi.co/api/v2/'


def get_pokemon_suggestions(num_pokemons: int):
    '''
    :param num_pokemons: int
    :return: a list of suggested pokemons
    '''
    url = f'{base_url}pokemon?limit={num_pokemons}&offset=2'
    request = requests.get(url)
    data = request.json()
    suggestions = data['results']
    return (suggestion['name'] for suggestion in suggestions)


def get_pokemon(name: str) -> dict:
    pokemon = requests.get(f'{base_url}/pokemon/{name}')
    if pokemon.status_code == 404:
        print('this pokemon cannot be found!')
        return dict()
    return pokemon.json()


def request_pokemon() -> dict[str, Any]:
    while True:
        pokemon_name = input('enter pokemon: '.title()).strip()
        if not pokemon_name: print('pokemon cannot be empty. please try again...'.capitalize())
        if pokemon_name: break
    pokemon = get_pokemon(pokemon_name)
    return pokemon


def main():
    pokemon = request_pokemon()
    while not pokemon:
        print('suggestions'.capitalize())
        pprint(suggested_pokemons)
        pokemon = request_pokemon()
    if not pokemon:
        return
    print('Pokemon Details')
    p = Pokemon(name=pokemon.get('name'), weight=pokemon.get('weight'), abilities=pokemon.get('abilities'))
    print(f'name: {p.name}'.title())
    print(f'weight: {p.weight}'.title())
    print('abilities'.capitalize())
    for ability in p.abilities:
        print(ability['ability']['name'], 'slots', ability['slot'])
    full_details = input(f'would you like to view full {p.name} full profile? [y/n]: ')
    if full_details.casefold() == 'y':
        print(json.dumps(pokemon, indent=2))



if __name__ == '__main__':
    suggested_pokemons = list(get_pokemon_suggestions(num_pokemons=10))
    main()
