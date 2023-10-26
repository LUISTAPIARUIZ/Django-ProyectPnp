from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Register

# Create your views here.
@login_required

def home(request):
    if request.method=='POST':
        print("added")
        #Retreive the user inputs
        register_roll=request.POST.get("register_roll")
        register_name=request.POST.get("register_name")
        register_email=request.POST.get("register_email")
        register_address=request.POST.get("register_address")
        register_phone=request.POST.get("register_phone")

        #create an object for models
        r=Register()
        r.roll=register_roll
        r.name=register_name
        r.email=register_email
        r.address=register_address
        r.phone=register_phone

        r.save()
        return redirect("home")
    register=Register.objects.all()
    return render(request, 'core/home.html', {'register': register})


def register(request):
    return render(request, 'core/register.html')

def analize(request):
    return render(request, 'core/analize.html')

def exit(request):
    logout(request)
    return redirect('home')
