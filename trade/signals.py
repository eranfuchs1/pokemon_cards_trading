from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserOwnedCards


def init_user_owned_cards(sender, instance, created, **kwargs):
    if created:
        user_owned_cards = UserOwnedCards.objects.create(user=instance)
        user_owned_cards.save()


post_save.connect(init_user_owned_cards, sender=User)
