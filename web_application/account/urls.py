from django.urls import path
from . import views

urlpatterns = [
    path('UserProfile',views.profile , name ='profile'),
    
]
