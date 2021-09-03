import requests
import trade.models as trade_models


url = 'https://pokeapi.co/api/v2/pokemon/'


def get_req_json_status(url):
    req_obj = requests.get(url)
    json_obj = req_obj.json()
    status_code = req_obj.status_code
    return req_obj, json_obj, status_code


def iterate_with_id(url, id_beg=0, func_for_json):
    req_obj, json_obj, status_code = get_req_json_status(f'{url}{id_beg}')
    while status_code == 200:
        func_for_json(json_obj)
        id_beg += 1
        req_obj, json_obj, status_code = get_req_json_status(f'{url}{id_beg}')


def store_json(json_obj):
    direct_json_dict = {}
    indirect_json_dict = {}
    for key in json_obj:
        if type(json_obj[key]) != type(json_obj):
            direct_json_dict[key] = json_obj[key]
        else:
            indirect_json_dict[key] = json_obj[key]
    card_model = trade_models.Card.objects.create(**direct_json_dict)


def store_cards(pickled_obj):
    for item in pickled_obj:
        card_model = trade_models.Card.objects.create(
            name=item['name'], base_experience=item['base_experience'], height=item['height'], weight=item['weight'])
        card_model.save()


# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile

# img_temp = NamedTemporaryFile(delete=True)
# img_temp.write(urllib2.urlopen(url).read())
# img_temp.flush()

# im.file.save(img_filename, File(img_temp))
