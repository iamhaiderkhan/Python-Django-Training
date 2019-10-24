from django.shortcuts import render
from django.views import View
from .forms import SignUpForm, UpdateProfileForm
from django.http import HttpResponseRedirect
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
            try:
                form.save()
                return HttpResponseRedirect('/auth/login/')
            except IntegrityError as e:
                return render(request, 'registration/signup.html', {'form': form, 'error': str(e).split('"')[1]})
        else:
            return render(request, 'registration/signup.html', {'form': form})


class ProfileUpdateView(View):

    def get(self, request):
        context = dict()
        context['form'] = UpdateProfileForm(instance=request.user)
        return render(request, 'registration/profile-update.html', context)

    def post(self, request):
        update_user_form = UpdateProfileForm(request.POST, instance=request.user)
        if update_user_form.is_valid():
            try:
                update_user_form.save()
                return HttpResponseRedirect('/')
            except IntegrityError:
                return render(request, 'registration/profile-update.html', update_user_form)
        else:
            return render(request, 'registration/signup.html', {'form': update_user_form})