from django.shortcuts import render, redirect

# Create your views here.
nav_links = ['homepage', ]

def homepage_view(request):
    context = {}
    context['nav_links'] = nav_links
    context['title'] = 'Trade Homepage'
    return render(request,'homepage.html', context=context)



from .forms import OfferTradeModelForm, PostTradeModelForm, TradeOfferAcceptModelForm
from .trade_offer import accept_and_remove, accept_trade_offer, post_trade, post_trade_offer, remove_trade_posting
from .models import Card, TradeOffer, TradePosting, UserOwnedCards
def card_collection_view(request):
    context = {}
    try:
        context['user_owned_cards'] = UserOwnedCards.objects.get(user=request.user.id)
    except UserOwnedCards.DoesNotExist:
        pass
    context['nav_links'] = nav_links
    context['title'] = 'Your Cards Collection'
    return render(request, 'card_collection.html', context=context)
def card_trade_posting_view(request):
    context = {}
    try:
        context['user_owned_cards'] = UserOwnedCards.objects.get(user=request.user.id)
    except UserOwnedCards.DoesNotExist:
        pass
    context['nav_links'] = nav_links
    context['title'] = 'Trade Posting'
    context['form'] = PostTradeModelForm()
    if request.method == 'GET':
        return render(request, 'trade_posting.html', context=context)
    elif request.method == 'POST':
        form = PostTradeModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
