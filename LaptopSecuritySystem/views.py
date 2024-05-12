from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import  CustomLoginForm
from django.contrib.auth.views import LoginView

    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'