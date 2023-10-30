from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    middle_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    #password = forms.CharField(max_length=30, required=True)
    user_type = forms.ChoiceField(choices=[(0, 'user'), (1, 'skimen')], required=True)


class LoginForm(forms.Form):
    email  = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)


