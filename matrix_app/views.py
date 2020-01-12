from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.forms import ModelForm  


def home(request):
    return render(request,'home.html')
def ulogin(request):
    return render(request,'user-login.html',{})
def dlogin(request):
    return render(request,'d-login.html',{})
def adminlogin(request):
    return render(request,'admin-login.html',{})
def registr(request):
    return render(request,'register.html',{})
def doctor_register(request):
    return render(request,'d-register.html',{})
def login(request):
    return render(request,'login.html',{})