import requests


def get_json(url):
    return requests.get(url).json()


def iterate_with_id(url, id_beg=0):
    json_obj = get_json(f'{url}{id_beg}')
    while json_obj:
        id_beg += 1
        json_obj = get_json(f'{url}{id_beg}')