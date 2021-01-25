import requests


def get_pokemon(num):
    resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num}').json()
    name = resp['species']['name']
    link_to_art = resp['sprites']['other']['official-artwork']['front_default']
    return {'name': name, 'img_link': link_to_art}
