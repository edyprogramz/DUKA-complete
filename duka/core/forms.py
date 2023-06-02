from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "your username",
        "class": "input-field"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "your password",
        "class": "input-field"
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "create a username",
        "class": "input-field"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "enter your email address",
        "class": "input-field"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "create a password",
        "class": "input-field"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "re-enter the password",
        "class": "input-field"
    }))