from django import forms
from django.core.validators import validate_email


class SignUpForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=30)
    email = forms.EmailField(max_length=254, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput())


