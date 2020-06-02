from django.shortcuts import render
import requests, json
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        secondname = request.POST.get('sname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname + '&lastName=' + secondname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joke': joke}
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'Bryan'
        secondname = 'Otieno'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + secondname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joke': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/contact.html')
    else:
         return render(request, 'mysite/contact.html')