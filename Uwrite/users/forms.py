from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "focus:outline-none", "placeholder": "mail@mail.com"}
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "focus:outline-none", "placeholder": "Enter username..."}
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "focus:outline-none", "placeholder": "Enter password"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "focus:outline-none", "placeholder": "Enter same password"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """Проверяет, существует ли уже пользователь с введенным email."""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Пользователь с этим email уже существует."
            )
        return email

  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'contact_number']


    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user