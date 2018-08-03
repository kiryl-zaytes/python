__author__ = 'Administrator'
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class Registration(FormView):
    template_name = 'udacity/registration.html'
    form_class = UserCreationForm
    success_url = '/udacity/wiki'

    def post(self, request):
        try:
            form = Registration.form_class(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/udacity/wiki')
        except (AttributeError, ValueError):
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


class SignIn(FormView):
    template_name = 'udacity/login_page.html'
    form_class = AuthenticationForm
    success_url = '/udacity/wiki'

    def post(self, request):
        form = SignIn.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            uauth = authenticate(username=username, password=password)
            if uauth.is_active:
                login(request, user=uauth)
                return HttpResponseRedirect('/udacity/wiki')
            else:
                return HttpResponse('user is not active')
        else:
            form = self.form_class()
            return render(request, SignIn.template_name, {'form': form})


class SignOut(View):

    def get(self, requets):
        logout(requets)
        return HttpResponseRedirect('/udacity/wiki')


class Success(View):
    def get(self, request):
        return render(request, '/udacity/wiki')