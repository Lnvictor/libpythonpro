import requests


def buscar_avatar(usuario):
    url = f'https://api.github.com/users/{usuario}'
    return requests.get(url).json()['avatar_url']

