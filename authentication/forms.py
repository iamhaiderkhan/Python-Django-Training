from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .mixins import EmailDuplicationMixin


class SignUpForm(EmailDuplicationMixin, forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=254,required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data.get('password'))
        user.save()
        return user


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateProfileForm(EmailDuplicationMixin, forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')