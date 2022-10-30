from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MyHomeView(View):
    def get(self, request):
        return render(request, 'home.html')


def menu(request):
    return render(request, 'main.html')
