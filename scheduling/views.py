from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
import logging
from categories.models import Categories
from stores.models import Stores

# Hiển thị danh sách đặt lịch
# @login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})

# Thêm mới lịch
# @login_required
def appointment_create(request):
    categories = Categories.objects.values('id', 'name')
    stores = Stores.objects.values('id', 'address')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # print(f"POST request payload: {form}")
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form, 'categories': categories, 'stores': stores})


def appointment_success(request):
    return render(request,'appointment_success.html')
