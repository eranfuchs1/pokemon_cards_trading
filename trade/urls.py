from django.urls import path
from .views import homepage_view, card_collection_view

urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('homepage/', homepage_view, name='homepage'),
    path('card_collection/', card_collection_view, name='card_collection'),
]
