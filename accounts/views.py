from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

# Create your views here.
class SignUpView(generic.CreateView): #subclass CreateView
    form_class = UserCreationForm     #puts to use a generic user creation form
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
