from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#MODULES FORMS
class CreateUserForm(UserCreationForm):
    
    email = forms.EmailField(required=True , label='Enter Company Email address',
                              widget=forms.EmailInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'email'
                                     
                                  })),
    first_name = forms.CharField(required=True , label='Enter Company Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))  
    username = forms.CharField(required=False , label='Enter User Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              )) 
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['first_name','email','username','password1','password2'] 
        
        
        
class NetworkProfileForm(ModelForm):
    city = forms.CharField(required=True , label='Enter City', 
                            widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    phoneNumber=forms.IntegerField( label='Enter Phone Number', required=True,                                )
    address = forms.CharField(label='Enter Address', required=False)

    capacity = forms.CharField(required=True , label='Enter Network Capacity', 
                            widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    IPAddress = forms.CharField(required=True , label='Enter Network IP', 
                            widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    Network = forms.ChoiceField(required=True,choices=NetworkProfile.network)
    Service = forms.ChoiceField(required=True,choices=NetworkProfile.service)
    profilePicture = forms.ImageField( required=False) 
   
    
    class Meta:
        model = NetworkProfile
        fields = ['city','phoneNumber','address','accountNumber','profilePicture','Service','Network',
                  'IPAddress','capacity']
   

#SPECIFIC FORMS  
    
  