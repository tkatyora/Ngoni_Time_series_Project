from django.shortcuts import render, redirect
from .models import *
from account.decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

#GENERAL MODULES  VIEWS

# collecting The Data from Database

first_slide = home.objects.first()
second_slide = home.objects.all()[1]
last_slide = home.objects.last()
@unauthenticated_user
def home(request):
    content ={}
    content ={
        'second_slide' : second_slide,
        'first_slide': first_slide,
        'last_slide': last_slide,
    }
    return render(request , 'Main/index.html' , content)

def about(request):
    content ={}
    content ={
        
    }
    
    return render(request , 'Main/about.html',content)


#SPECIFIC MODULES VIEWS





