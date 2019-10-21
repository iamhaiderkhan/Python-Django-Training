from django import forms
from django.contrib.auth.models import User
from .exception import DuplicateEmailError


class EmailDuplicationMixin(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email already exist, please try another email')
        return email



