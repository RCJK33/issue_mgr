from django.shortcuts import render
from .forms import UserCreationForm
from django.urls import reverse

from django.views.generic import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse('issues_list')