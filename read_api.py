import requests


url = 'https://pokeapi.co/api/v2/pokemon/'


def get_req_json_status(url):
    req_obj = requests.get(url)
    json_obj = req_obj.json()
    status_code = req_obj.status_code
    return req_obj, json_obj, status_code


def iterate_with_id(url, id_beg=0):
    req_obj, json_obj, status_code = get_req_json_status(f'{url}{id_beg}')
    while status_code == 200:
        id_beg += 1
        req_obj, json_obj, status_code = get_req_json_status(f'{url}{id_beg}')
