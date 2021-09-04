from django.urls import path
from .views import LoginView, SignupView, profile_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile_redirect'),
]
