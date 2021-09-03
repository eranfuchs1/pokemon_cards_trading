import pickle
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cards.settings")

django.setup()

from trade.models import Card, Abilities, Forms, Item, Move, Species, Sprites

key_to_modelclass = {
    'abilities': Abilities,
    'forms': Forms,
    'held_items': Item,
    'moves': Move,
    'species': Species,
    'sprites': Sprites,
}



key_to_field = {
    'abilities': 'ability',
    'forms': 'name',
    'held_items': 'name',
    'moves': 'name',
    'species': 'name',
    'sprites': 'front_default',
}


keys_of_arrays = {
    'abilities': [0, 'ability', 0, 'name', ],
    'forms': [0, 'name', ],
    'held_items': [0, 'item', 'name', ],
    'moves': [0, 'move', 'name', ],
}

key_to_karr = {
    'abilities': [0, 'ability', 0, 'name', ],
    'forms': [0, 'name', ],
    'held_items': [0, 'item', 'name', ],
    'moves': [0, 'move', 'name', ],
    'species': ['name', ],
    'sprites': ['front_default', ],
}

def get_by_key_array(obj, karr):
    if len(karr) > 0:
        return get_by_key_array(obj[karr[0]], karr[1:])
    else:
        return obj






def store_cards(pickled_obj):
    for item in pickled_obj:
        card_model = Card.objects.create(
            id=item['id'], name=item['name'], base_experience=item['base_experience'], height=item['height'], weight=item['weight'])
        card_model.save()


def store_cards_foreign_keys(pickled_obj):
    for index, item in enumerate(pickled_obj):
        for key in item:
            if key in key_to_modelclass:
                print(f'    index{index}')
                card_model = Card.objects.get(name=item['name'])
                if type(item[key]) == type(list([1,2,3])):
                    for val in item[key]:
                        if 'name' in val:
                            kwarg = {key_to_field[key]:val['name']}
                        elif 'ability' in val:
                            kwarg = {key_to_field[key]:val['ability']}
                        else:
                            continue
                        foreign_model = key_to_modelclass[key].objects.create(**kwarg)
                        foreign_model.save()
                        if key == 'abilities':
                            card_model.abilities.add(foreign_model)
                        elif key == 'forms':
                            card_model.forms.add(foreign_model)
                        elif key == 'held_items':
                            card_model.held_items.add(foreign_model)
                        elif key == 'moves':
                            card_model.moves.add(foreign_model)
                        elif key == 'species':
                            card_model.species.add(foreign_model)
                        elif key == 'sprites':# image handling
                            card_model.sprites.add(foreign_model)
                        card_model.save()
                else:
                    if 'name' in item[key]:
                        kwarg = {key_to_field[key]:item[key]['name']}
                    elif 'front_default' in item[key]:
                        kwarg = {key_to_field[key]:item[key]['front_default']}
                    else:
                        continue
                    foreign_model = key_to_modelclass[key].objects.create(**kwarg)
                    foreign_model.save()
                    if key == 'abilities':
                        card_model.abilities.add(foreign_model)
                    elif key == 'forms':
                        card_model.forms.add(foreign_model)
                    elif key == 'held_items':
                        card_model.held_items.add(foreign_model)
                    elif key == 'moves':
                        card_model.moves.add(foreign_model)
                    elif key == 'species':
                        card_model.species.add(foreign_model)
                    elif key == 'sprites':# image handling
                        card_model.sprites.add(foreign_model)
                    card_model.save()
                    '''
                for value in item[key]:
                    print(key_to_field[key])
                    kwargs = {key_to_field[key] : get_by_key_array(item, key_to_karr[key])}
                    foreign_model = key_to_modelclass[key].objects.create(**kwargs)
                    foreign_model.save()
                    if key == 'abilities':
                        card_model.abilities.add(foreign_model)
                    elif key == 'forms':
                        card_model.forms.add(foreign_model)
                    elif key == 'held_items':
                        card_model.held_items.add(foreign_model)
                    elif key == 'moves':
                        card_model.moves.add(foreign_model)
                    elif key == 'species':
                        card_model.species.add(foreign_model)
                    elif key == 'sprites':# image handling
                        card_model.sprites.add(foreign_model)
                card_model.save()
                    '''


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rb') as fb:
        pickled_obj = pickle.load(fb)
    # store_cards(pickled_obj)
    store_cards_foreign_keys(pickled_obj)
