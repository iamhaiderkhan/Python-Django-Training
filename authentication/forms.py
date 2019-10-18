from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')









