from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserSignupForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


def profile_view(request):
    return redirect('homepage')
