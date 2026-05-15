from django.views.generic import CreateView
from .forms import UserCreationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

#Create your views here.
class Register(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    success_message = "Account created successfully."

class Login(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_message = 'You are now logged in.'
    success_url = reverse_lazy('login')