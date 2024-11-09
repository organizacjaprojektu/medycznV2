# clinic_app/urls.py
# clinic_app/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.login_view, name='login'),  # Dodaj ścieżkę dla strony głównej
]
