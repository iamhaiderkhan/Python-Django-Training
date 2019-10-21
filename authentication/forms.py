from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def email_clean(self, new_email):
        try:
            email = User.objects.filter(email=new_email).count()
            return email
        except ObjectDoesNotExist:
            pass


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def email_clean(self, new_email, user_id):
        try:
            email = User.objects.filter(email=new_email).exclude(id=user_id).count()
            return email
        except ObjectDoesNotExist:
            pass










