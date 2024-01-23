from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models import Q

class NetworkProfile(models.Model):
    #MODULES FILEDS
        network = [('VSAT','VSAT'),('Fibre','Fibre')]
        service = [('customer','Customer'),('Admin','Telone Admin')]
        user = models.OneToOneField(User, verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
        phoneNumber = models.CharField(max_length=100,null=True)
        city = models.CharField(max_length=100,null=True,default='Not Selected')
        address = models.CharField(max_length=50, null= True,blank=True) 
        accountNumber = models.CharField(max_length=200,null=True)    
        capacity = models.CharField(max_length=200,null=True,blank=False)
        IPAddress = models.CharField(max_length=100,null= True,blank=False)
        Network  =models.CharField(max_length=100,null= True,blank=False,choices=network)
        Service =models.CharField(max_length=100,null= True,blank=False,choices=service)
        profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        
        # class Meta:
        #       constraints = [
        #             models.CheckConstraint(
        #                   check=Q(networkAdmin = True ,customer = False ) | Q(networkAdmin = False ,customer = True ),
        #                   name= 'one_true_one_false',
        #             )
        #       ]
        @property
        def ImageUrl(self):
            try:
                url = self.profilePicture.url
            except:
                url = ''
                
            return url
        def __str__(self):
                return f"Company Name: {(self.user.first_name)} "
        
