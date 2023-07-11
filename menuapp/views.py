from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menuapp/menu.html')