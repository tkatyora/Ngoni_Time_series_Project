from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback_Complains(models.Model):
    Type = [('Complain','Complain'),('Feedback','Feedback')]
    type = models.CharField(max_length=50,null=True,blank=False,choices = Type)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
    updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    created_by = models.ForeignKey(User,  on_delete=models.CASCADE ,null=True,blank=True)
    reply = models.CharField(max_length=50,null=True,blank=True, default='None')

    def __str__(self):
        return f'Feedback for  { str(self.type)}'

    class meta:
        ordering = ('-created',)

class recomandations(models.Model):
    Type = [('1','Level1'),('2','Level2'),('3','Level3'),('4','Level4')]
    type = models.CharField(max_length=50,null=True,blank=False,choices = Type)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
    updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)

    def __str__(self):
        return f'Recomdation of Level { str(self.type)}'

    class meta:
        ordering = ('-created',)