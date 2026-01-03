from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import SignupModel

class SignupForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True, max_length=30)
    contact_no = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=10)
    cnf_password = forms.CharField(required=True, max_length=10)


    class Meta:
        model = SignupModel
        fields = [
            'username',
            'email',
            'contact_no',
            'password',
            'cnf_password'
        ]