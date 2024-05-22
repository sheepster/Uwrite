from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class New_User_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        field = ("username", "email", "password1", "password2")