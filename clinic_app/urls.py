"""
URL configuration for clinic_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# clinic_app/urls.py
from django.contrib import admin
from django.urls import path, include

# clinic_app/urls.py

from django.urls import path, include

import accounts.views
from accounts import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('add_room/', views.add_room, name='add_room'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('change_reservation/<int:reservation_id>/', views.change_reservation, name='change_reservation'),
    path('view_rooms/', views.view_rooms, name='view_rooms'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('view_reservations/', views.view_reservations, name='view_reservations'),
]