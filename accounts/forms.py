from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', ]
