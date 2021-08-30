from django.db import models

# Create your models here.
__card_text_max_length = 100

class Card(models.Model):
    title = models.CharField(max_length=__card_text_max_length)
    image = models.ImageField()

