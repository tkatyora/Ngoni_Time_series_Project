from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models import Q

class NetworkProfile(models.Model):
    #MODULES FILEDS
        network = [('VSAT','VSAT'),('Fibre','Fibre')]
        service = [('customer','Customer'),('Admin','GNP Admin')]
        user = models.OneToOneField(User, verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
        phoneNumber = models.CharField(max_length=100,null=True,blank = True)
        city = models.CharField(max_length=100,null=True,default='Not Selected')
        address = models.CharField(max_length=50, null= True,blank=True) 
        accountNumber = models.CharField(max_length=200,null=True)    
        capacity = models.CharField(max_length=200,null=True,blank=True)
        IPAddress = models.CharField(max_length=100,null= True,blank=True)
        Network  =models.CharField(max_length=100,null= True,blank=True,choices=network)
        Service =models.CharField(max_length=100,null= True,blank=True,choices=service)
        profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        
     
        @property
        def ImageUrl(self):
            try:
                url = self.profilePicture.url
            except:
                url = ''
                
            return url
        def __str__(self):
                return f"Company Name: {(self.user.first_name)} "
        
