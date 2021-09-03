from django.urls import path
from .views import homepage_view

urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('homepage/', homepage_view, name='homepage')
]
