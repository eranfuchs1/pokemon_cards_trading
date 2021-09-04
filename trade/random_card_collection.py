import random
from .models import Card


def random_card_collection(num_of_cards=10):
    all_cards = list(Card.objects.all())
    random.shuffle(all_cards)
    random_cards = all_cards[:num_of_cards]
    return random_cards
