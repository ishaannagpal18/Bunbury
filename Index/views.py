from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        whatsapp = request.POST.get('whatsapp')
        age = request.POST.get('age')
        city = request.POST.get('city')
        date = request.POST.get('date')
        auth_token = str(uuid.uuid4())[:8]
        register_obj = Register.objects.create(name = name , auth_token=auth_token, email=email, contact = contact, whatsapp = whatsapp,age=age, city=city, date=date)
        html_template = render_to_string('register_email.html', {'name':name, 'auth_token':auth_token, 'date':date})
        recipient_list = [email]
        message = EmailMessage('Welcome To BUNBURY', html_template,
                                   'BUNBURY <info@bunbury.in>', [email])
        message.content_subtype = 'html'
        message.send()
        register_obj.save()
        messages.success(request, 'Registered Sucessfully')



        return HttpResponseRedirect(reverse('home'))


    return render(request, 'register.html')

def test(request):
    bday = Birthday.objects.order_by('id').last()
    print(bday)
    if request.method == 'POST' and request.FILES['image']:
        name = request.POST.get('name')
        image = request.FILES.get('image')
        bday_obj = Birthday.objects.create(name=name,image=image)
        bday_obj.save()
        return HttpResponseRedirect(reverse('test'))
    return render(request, 'test.html', {'bday':bday})
