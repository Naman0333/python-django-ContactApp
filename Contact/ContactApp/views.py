from django.shortcuts import render
from django.contrib import messages
from . models import  Contact
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your profile is added..!!!')

    return render(request,'contact.html')
