# forms.py
from django import forms
from .models import Laptop, Student, Staff, Guest

# Define common style for form inputs
input_style = {
    'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light'
}

class LaptopRegistrationForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        required=False,
        widget=forms.Select(attrs=input_style)
    )
    staff = forms.ModelChoiceField(
        queryset=Staff.objects.all(),
        required=False,
        widget=forms.Select(attrs=input_style)
    )
    guest = forms.ModelChoiceField(
        queryset=Guest.objects.all(),
        required=False,
        widget=forms.Select(attrs=input_style)
    )

    class Meta:
        model = Laptop
        fields = ['laptop_name', 'model', 'serial_number', 'color', 'student', 'staff', 'guest']
        widgets = {
            'laptop_name': forms.TextInput(attrs=input_style),
            'model': forms.TextInput(attrs=input_style),
            'serial_number': forms.TextInput(attrs=input_style),
            'color': forms.TextInput(attrs=input_style),
            # Add other fields if necessary
        }


    def __init__(self, *args, **kwargs):
        super(LaptopRegistrationForm, self).__init__(*args, **kwargs)
        # Initialize your form fields here, if needed
