from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.forms import ModelForm 
from .models import dr_register,usr_register 
from django.core.files.uploadhandler import MemoryFileUploadHandler , TemporaryFileUploadHandler
from django.core.files.storage import FileSystemStorage 

from .forms import doctor_r,usr_r,usr_login,dr_login
def home(request):
    return render(request,'home.html')
    



def ulogin(request):
    if request.method == 'POST':
            if usr_register.objects.filter(user_name = request.POST['user_name'],password1 = request.POST['password1']):
                return redirect("/")
            else:
                messages.info(request,"username or password not matched")
                return redirect("/user-login/")

    else:
        form = usr_login()
    return render(request,'user-login.html',{'forms':form})

    return render(request,'user-login.html',{})
def dlogin(request):
    if request.method == 'POST':
            if dr_register.objects.filter(username = request.POST['username'],password1 = request.POST['password1']):
                return redirect("/")
            else:
                messages.info(request,"username or password not matched")
                return redirect("/doctor-login/")

    else:
        form = dr_login()
    return render(request,'d-login.html',{'forms':form})

    return render(request,'d-login.html',{})
def adminlogin(request):
    return render(request,'admin-login.html',{})
def registr(request):
    return render(request,'register.html',{})
def doctor_register(request):
    if request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            messages.info(request,"password not matched")
            return redirect('/doctor-register/')
        else:
            if dr_register.objects.filter(username = request.POST['username']):
                messages.info(request,"username already taken")
                return redirect("/doctor-register/")
            else:
                form = doctor_r(request.POST or None ,request.FILES or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    print("uploaded")
                    return redirect('/')
                else:
                    return redirect("/doctor-register/")
    else:
        form = doctor_r()
    return render(request,'d-register.html',{'forms':form})

def login(request):
    
    return render(request,'login.html',{})
def u_register(request):
    if request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            messages.info(request,"password not matched")
            return redirect('/user-register/')
        else:
            if usr_register.objects.filter(user_name = request.POST['user_name']):
                messages.info(request,"username already taken")
                return redirect("/user-register/")
            else:
                form = usr_r(request.POST or None ,request.FILES or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    print("uploaded")
                    return redirect('/')
                else:
                    return redirect("/user-register/")
    else:
        form = usr_r()
    return render(request,'u-register.html',{'forms':form})