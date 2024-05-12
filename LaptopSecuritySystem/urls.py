from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),


    path('accounts/login/', CustomLoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
