from django import forms
from django.forms.models import ModelForm
from .models import Card, UserOwnedCards, TradeOffer, TradePosting
class PostTradeModelForm(ModelForm):
    class Meta():
        model = TradePosting
        fields = ['cards_posted', ]
class OfferTradeModelForm(ModelForm):
    class Meta():
        model = TradeOffer
        fields = ['cards_offered', ]
class TradeOfferAcceptModelForm(ModelForm):
    class Meta():
        model = TradePosting
        fields = ['trade_offers', ]
