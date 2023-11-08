from django import forms
from .models import *
from equipment.models import Staff

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30,label='Name', required=True)
    middle_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Прізвище' }))
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
  
    USER_CHOICES = [(0, 'User'), (1, 'Skimen')]
    user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect, required=True, initial=0)
    terms = forms.BooleanField(required=False)

    user_type.widget.attrs['placeholder'] = 'Select User Type'

class LoginForm(forms.Form):
    email  = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class StaffAddForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['brend','model','year_of_pruduction','type','count']




