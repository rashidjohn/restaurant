from django.shortcuts import render
from .models import *
from .forms import ContactForm, BookingForm

# Create your views here.
def contactView(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {
        'form':form
    }

    return render(request, 'contactapp/contact.html', context)

def teamView(request):
    team = Team.objects.all()
    context = {
        'team':team
    }
    return render(request, 'contactapp/team.html', context)
