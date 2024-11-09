# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'doctor':
                return redirect('doctor_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
# accounts/views.py

# accounts/views.py
from django.shortcuts import render



# Widoki dla admina
# clinic/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Room, Staff, Reservation
from .forms import RoomForm, StaffForm, ReservationForm

# Widoki dla admina
@permission_required('clinic.manage_room', raise_exception=True)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_rooms')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

@permission_required('clinic.manage_staff', raise_exception=True)
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    else:
        form = StaffForm()
    return render(request, 'add_staff.html', {'form': form})

@permission_required('clinic.manage_reservation', raise_exception=True)
def change_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'change_reservation.html', {'form': form})

# Widoki dla doktora
def view_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'view_rooms.html', {'rooms': rooms})

def view_staff(request):
    staff = Staff.objects.all()
    return render(request, 'view_staff.html', {'staff': staff})


def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.doctor = request.user
            reservation.save()
            return redirect('view_reservations')
    else:
        form = ReservationForm()
    return render(request, 'add_reservation.html', {'form': form})

def view_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'view_reservation.html', {'reservations': reservations})
