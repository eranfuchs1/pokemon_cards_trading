from .models import TradeOffer
from .models import TradePosting
from .models import UserOwnedCards
def post_trade(user, cards):
    trade_posting = TradePosting.objects.create(trade_poster=user)
    trade_posting.cards_posted.add(cards)
    trade_posting.save()
def post_trade_offer(user, cards, trade_posting):
    trade_offer = TradeOffer.objects.create(user=user)
    trade_offer.cards_offered.add(cards)
    trade_offer.save()
    trade_posting.trade_offers.add(trade_offer)
    trade_posting.save()
def accept_trade_offer(trade_posting, trade_offer):
    user_poster_cards = UserOwnedCards.objects.get(user=trade_posting.trade_poster)
    user_offer_cards = UserOwnedCards.objects.get(user=trade_offer.user)
    user_poster_cards_offer = []
    for card in trade_posting.cards_posted.all():
        user_poster_cards.cards.remove(user_poster_cards.cards.filter(name=card.name)[0])
        user_offer_cards.cards.add(card)
    for card in trade_offer.cards_offered.all():
        user_offer_cards.cards.remove(user_offer_cards.cards.filter(name=card.name)[0])
        user_poster_cards.cards.add(card)
    user_offer_cards.save()
    user_poster_cards.save()
def remove_trade_posting(trade_posting):
    trade_posting.delete()
    trade_posting.save()
def accept_and_remove(trade_posting, trade_offer):
    accept_trade_offer(trade_posting, trade_offer)
    remove_trade_posting(trade_posting)
