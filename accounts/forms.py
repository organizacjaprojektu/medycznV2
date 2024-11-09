# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
# clinic/forms.py
from django import forms
from .models import Room, Staff, Reservation

# clinic/forms.py
from django import forms
from .models import Room, Staff, Reservation

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'role']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'staff', 'date', 'time']
