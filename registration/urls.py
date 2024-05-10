# urls.py

from django.urls import path
from .views import register_laptop, dashboard_view, registration_success

urlpatterns = [
    path('register/', register_laptop, name='register_laptop'),
    path('', dashboard_view, name='dashboard'),
    path('registration-success/<int:laptop_id>/', registration_success, name='registration_success'),
    # Other URL patterns...
]
