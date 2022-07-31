from django.shortcuts import render
from instrument.models import Instrument
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    instruments = Instrument.objects.all()
    context = {
        'instruments' : instruments,
    }
    return render(request, 'home.html', context)

def team(request):
    return render(request,'team.html', {})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = "From: " + from_email + "\n\n" + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bioequipzon@gmail.com'])
            except BadHeaderError:
                return render(request,'contact.html')
            return redirect('home')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return render(request,'home.html')