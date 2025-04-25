import requests
import json
from pokemon_class import Pokemon

base_url: str = 'https://pokeapi.co/api/v2/'


def get_pokemon_hint(limit: int):
    '''

    :param limit: int
    :return: a list of suggested pokemons
    '''
    url = f'{base_url}pokemon?limit={limit}&offset=2'
    request = requests.get(url)
    data = request.json()
    suggestions = data['results']
    return (suggestion['name'] for suggestion in suggestions)


def get_pokemon(name: str):
    pokemon = requests.get(f'{base_url}/pokemon/{name}')
    if pokemon.status_code == 404:
        print('this pokemon cannot be found!')
        return dict()
    return pokemon.json()


def request_pokemon():
    pokemon_name: str = input('enter pokemon: '.title()).strip()
    pokemon = get_pokemon(pokemon_name)
    return pokemon


def main():
    suggested_pokemons = list(get_pokemon_hint(2))

    pokemon = request_pokemon()
    while not pokemon:
        print('suggestions'.capitalize())
        print(suggested_pokemons)
        pokemon = request_pokemon()

    if pokemon:
        # print(json.dumps(pokemon, indent=2))
        print('Pokemon Details')
        p = Pokemon(name=pokemon.get('name'), weight=pokemon.get('weight'), abilities=pokemon.get('abilities'))
        print(f'name: {p.name}'.title())
        print(f'weight: {p.weight}'.title())
        print('abilities'.capitalize())
        for ability in p.abilities:
            print(ability['ability']['name'], 'slots', ability['slot'])


if __name__ == '__main__':
    main()
