from django.urls import path
from .views import homepage_view, card_collection_view, card_trade_posting_view, trade_posts_view

urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('homepage/', homepage_view, name='homepage'),
    path('card_collection/', card_collection_view, name='card_collection'),
    path('trade_posting/', card_trade_posting_view, name='trade_posting'),
    path('trade_posts/', trade_posts_view, name='trade_posts'),
]
