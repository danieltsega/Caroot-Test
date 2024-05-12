from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):
    
    def get_invalid_login_error(self):
        return forms.ValidationError(
            _("Incorrect username or password."),
            code='invalid_login'
        )
    
    
    """    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Enter Email...'
    }), label='')
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter UserName...'
    }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200 mb-4',
        'placeholder': 'Enter Password...'
    }), label='Password')
    
    
    class Meta:
        model = User
        fields = ['username', 'password']
        error_message = ''