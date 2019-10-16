from django.shortcuts import render
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# from django.db.utils import IntegrityError
from django.db.utils import IntegrityError

# Create your views here.


class AuthenticationView(View):
    def get(self, request):
        return render(request, 'home.html')


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()

        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form_data = form.clean()
            new_user_data = {
                'username': form_data.get('username'),
                'email': form_data.get('email'),
                'password': form_data.get('password')
            }
            try:
                User.objects.create_user(new_user_data['username'], new_user_data['email'], new_user_data['password'])
                return HttpResponseRedirect('/')
            except IntegrityError as e:
                return render(request, 'registration/signup.html', {'form': form, 'error': str(e).split('"')[1]})













