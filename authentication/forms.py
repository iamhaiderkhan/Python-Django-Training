from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .exception import DuplicateEmailError
from django.contrib.auth.hashers import make_password


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def email_clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise DuplicateEmailError()
        return email

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data.get('password'))
        user.save()
        return user


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def email_clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise DuplicateEmailError()
        return email

    def save(self):
        user = super(UpdateProfileForm, self).save(commit=False)
        user.save()
        return user
