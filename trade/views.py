from .models import Card, TradeOffer, TradePosting, UserOwnedCards
from .trade_offer import accept_and_remove, accept_trade_offer, post_trade, post_trade_offer, remove_trade_posting
from .forms import OfferTradeModelForm, PostTradeModelForm, TradeOfferAcceptModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
nav_links = ['homepage', 'card_collection', 'trade_posting', 'trade_posts', 'trade_offers', ]


def homepage_view(request):
    context = {}
    context['nav_links'] = nav_links
    context['title'] = 'Trade Homepage'
    return render(request, 'homepage.html', context=context)


@login_required
def card_collection_view(request):
    context = {}
    try:
        context['user_owned_cards'] = UserOwnedCards.objects.get(
            user=request.user.id)
    except UserOwnedCards.DoesNotExist:
        pass
    context['nav_links'] = nav_links
    context['title'] = 'Your Cards Collection'
    return render(request, 'card_collection.html', context=context)


@login_required
def card_trade_posting_view(request):
    context = {}
    try:
        context['user_owned_cards'] = UserOwnedCards.objects.get(
            user=request.user.id)
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
            trade_posting = form.save(commit=False)
            trade_posting.trade_poster = request.user
            trade_posting.save()
            form.save()
        return redirect('homepage')


def trade_posts_view(request):
    context = {}
    context['nav_links'] = nav_links
    context['title'] = 'Trade Posts'
    context['trade_posts'] = TradePosting.objects.all()
    return render(request, 'trade_posts.html', context=context)


def trade_offer_view(request, trade_post_id):
    context = {}
    context['nav_links'] = nav_links
    context['title'] = 'Post Trade Offer'
    try:
        context['user_owned_cards'] = UserOwnedCards.objects.get(
            user=request.user.id)
    except UserOwnedCards.DoesNotExist:
        pass
    context['posted_trade_cards'] = TradePosting.objects.get(id=trade_post_id)
    context['form'] = OfferTradeModelForm()
    if request.method == 'GET':
        return render(request, 'trade_offer.html', context=context)
    elif request.method == 'POST':
        form = OfferTradeModelForm(request.POST)
        if form.is_valid():
            trade_offer = form.save(commit=False)
            trade_offer.user = request.user
            trade_offer.save()
            form.save()
            context['posted_trade_cards'].trade_offers.add(trade_offer)
            context['posted_trade_cards'].save()

        return redirect('homepage')

@login_required
def trade_offers_view(request):
    context = {}
    context['nav_links'] = nav_links
    context['title'] = 'Trade Offers'
    context['trade_posts'] = TradePosting.objects.filter(trade_poster=request.user)
    return render(request, 'trade_offers.html', context=context)
