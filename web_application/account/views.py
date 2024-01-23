from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from account.models import *
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate,login,logout
from .form import *

#DJANGO MODULES
# Create your views here.
AllProfile = NetworkProfile.objects.all()
alluser = User.objects.all() 
print(AllProfile)
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


@unauthenticated_user
#Account Creation
def RegesterClient(request):
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        if userForm.is_valid():
            client = userForm.save(commit=False)
            name = userForm.cleaned_data.get('fisrt_name')
            print(name)
            print(str(name))
            Companyusername = str(name)+'@tel1'
            client.username = Companyusername
            client.save()
            message = 'Account for',{Companyusername},'have been succesfully created'
            messages.success(request,message )
            login(request, client)
            return redirect('dashboard')
        else:
            messages.warning(request,'User Form Is Not Valid' )
            return redirect('create_account')           
    else:
        userForm = CreateUserForm()  
    content={}
    content = {
        'CompanyForm' : userForm 
    }
    return render(request, 'Accounts/regester.html' , content)


login_required(login_url='sign_in')
def newClient(request):
    if request.method == 'POST':
        NetworkForm = NetworkProfileForm(request.POST)
        if NetworkForm.is_valid():
            NetworkForm.save()
            
            message = 'Account for',{username},'have been succesfully created'
            messages.success(request,message )
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request,'User Form Is Not Valid' )
            return redirect('create_client')           
    else:
       
        NetworkForm = NetworkProfileForm()
        
    content={}
    content = {
        
        'networkForm': NetworkForm}
    return render(request, 'Accounts/ClientRegistration.html' , content)


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


@login_required(login_url='sign_in') 
def updateProfile(request,pk):
    profileToBeUpdated = Profile.objects.get(id = pk) 
    userToBeUpdated = User.objects.get(id = pk) 
    if request.method == 'POST':
        form = CreateProfileForm(request.POST ,instance =profileToBeUpdated )
        userform = CreateUserForm(request.POST ,instance =userToBeUpdated )
        if form.is_valid():
            form.save()
            if userform.is_valid():
                userform.save()
                messages.success(request,'Profile Updated Succesfully')
                return redirect('profile') 
            else:
                messages.warning(request, 'Error Encountered In Updating Profile2')
                #return redirect('dashboard') 
        else:
            messages.warning(request, 'Error Encountered In Updating Profile1')
            #return redirect('dashboard')
    else:
        form = CreateProfileForm(instance=profileToBeUpdated)
        userform = CreateUserForm(instance=userToBeUpdated)
        
    content ={}
    content ={
        'form' : form,
        'userform' : userform,
        'profile':AllProfile,
        'users':alluser
    }
    
    
    return render(request,  'updateProfile.html', content)

@login_required(login_url='sign_in')   
def deleteProfile(request,pk):
    deletedProfile = Profile.objects.get(id=pk)
    if request.method =='POST':
        request.user.delete()
        #deletedProfile.delete()
        ##print(user)
        message = messages.success(request, 'Account Succusefully Deleted')
        return redirect('sign_in')
    else:
       message =  messages.warning(request, 'Failled to delete Account')
        
    content={}
    content ={
        'deletedProfile':AllProfile
    }
    return render(request,'deleteProfile.html',content)

