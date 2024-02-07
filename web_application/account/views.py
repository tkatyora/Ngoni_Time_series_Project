from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from account.models import *
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate,login,logout
from .form import *


# Create your views here.
AllProfile = NetworkProfile.objects.all()
alluser = User.objects.all() 

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        if User is not None:
            login(request, User)
            messages.success(request, 'Log  Successfully')
            return redirect('dashboard') 
        else:
            messages.warning(request, 'Invalid Username or  Paasword')
            return redirect('sign_in')
                      
    return render(request, 'Accounts/Usernamelogin.html' )


@login_required(login_url='sign_in') 
def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')

@login_required(login_url='sign_in') 
def profile(request):
    content ={}
    content ={
        'profiles':AllProfile,
        'users': alluser
    }
    return render(request , 'Accounts/profile.html',content)


