from django.shortcuts import render, redirect
from contactapp.forms import BookingForm
from contactapp.models import Booking
from .models import *

# Create your views here.
def home(request):
    food_b = Menu.objects.filter(type='breakfast')[:1]
    food_d = Menu.objects.filter(type='dinner')[:1]
    food_l = Menu.objects.filter(type='launch')[:1]
    form = BookingForm()
    if request.method == 'POST':
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    context = {
        'form':form,
        'food_b':food_b,
        'food_d':food_d,
        'food_l':food_l,
    }
    return render(request, 'menuapp/index.html', context)

def menu(request):
    food_b = Menu.objects.filter(type='breakfast')
    food_d = Menu.objects.filter(type='dinner')
    food_l = Menu.objects.filter(type='launch')
    context = {
        'food_b':food_b,
        'food_d':food_d,
        'food_l':food_l,
    }
    return render(request, 'menuapp/menu.html', context)