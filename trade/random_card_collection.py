import random
from .models import Card


def random_card_collection():
    all_cards = list(Card.objects.all())
    random.shuffle(all_cards)
    random_cards = all_cards[:10]
    return random_cards
