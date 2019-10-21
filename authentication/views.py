from django.shortcuts import render
from django.views import View
from .forms import SignUpForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.db.utils import IntegrityError
from .exception import DuplicateEmailError
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
        print(form.is_valid())
        if form.is_valid():

            form_data = form.clean()

            new_user_data = {
                    'username': form_data.get('username'),
                    'email': form_data.get('email'),
                    'password': form_data.get('password')
            }

            user_other_fields = {
                'first_name': form_data.get('first_name'),
                'last_name': form_data.get('last_name'),
            }
            try:
                email = form.email_clean(form_data.get('email'))
                if email:
                    raise DuplicateEmailError("Email already exist, please try another email")

                User.objects.create_user(
                    new_user_data['username'],
                    new_user_data['email'],
                    new_user_data['password'],
                    **user_other_fields)

                return HttpResponseRedirect('/auth/login/')
            except IntegrityError as e:
                return render(request, 'registration/signup.html', {'form': form, 'error': str(e).split('"')[1]})
            except DuplicateEmailError as e:
                return render(request, 'registration/signup.html', {'form': form, 'error': e})
        else:
            form = SignUpForm(request.POST)
            return render(request, 'registration/signup.html', {'form': form})


class ProfileUpdateView(View):

    def get(self, request):
        form_data = {}
        pre_user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name

        }
        form_data['form'] = UpdateProfileForm(pre_user_data)
        return render(request, 'registration/profile-update.html', form_data)

    def post(self, request):
        data = {}
        update_user_form = UpdateProfileForm(request.POST, instance=request.user)
        if update_user_form.is_valid():
            try:

                email = update_user_form.email_clean(update_user_form.cleaned_data.get('email'), request.user.id)
                if email:
                    raise DuplicateEmailError("Email already exist, please try another email")

                update_user_form.save()
                return HttpResponseRedirect('/')
            except IntegrityError as e:
                data['form'] = update_user_form
                data['error'] = e
                return render(request, 'registration/profile-update.html', data)
            except DuplicateEmailError as e:
                data['form'] = update_user_form
                data['error'] = e
                return render(request, 'registration/profile-update.html', data)