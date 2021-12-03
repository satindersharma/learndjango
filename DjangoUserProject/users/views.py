from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'



class UserLoginView(LoginView):
    pass


class UserLogoutView(LogoutView):
    pass
