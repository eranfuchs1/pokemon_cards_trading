from django.db import models
from django.contrib.auth.models import User

# Create your models here.

card_text_max_length = 300




class Abilities(models.Model):
    ability = models.CharField(max_length=card_text_max_length)


class Forms(models.Model):
    name = models.CharField(max_length=card_text_max_length)


class Item(models.Model):
    name = models.CharField(max_length=card_text_max_length)


class Move(models.Model):
    name = models.CharField(max_length=card_text_max_length)


class Species(models.Model):
    name = models.CharField(max_length=card_text_max_length)


class Sprites(models.Model):
    front_default = models.URLField()


class Card(models.Model):
    name            = models.CharField(max_length=card_text_max_length, null=True)
    base_experience = models.IntegerField(null=True)
    height          = models.IntegerField(null=True)
    weight          = models.IntegerField(null=True)
    abilities       = models.ManyToManyField(Abilities)
    forms           = models.ManyToManyField(Forms)
    held_items      = models.ManyToManyField(Item)
    moves           = models.ManyToManyField(Move)
    species         = models.ManyToManyField(Species)
    sprites         = models.ManyToManyField(Sprites)



class UserOwnedCards(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    cards         = models.ManyToManyField(Card)



class TradeOffer(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    cards_offered = models.ManyToManyField(Card)


class TradePosting(models.Model):
    trade_poster  = models.ForeignKey(User, on_delete=models.CASCADE)
    cards_posted  = models.ManyToManyField(Card)
    trade_offers  = models.ManyToManyField(TradeOffer)
