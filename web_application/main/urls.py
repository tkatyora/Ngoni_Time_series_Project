from django.urls import path
from . import views
from account import views as view

urlpatterns = [
    #Django Modules
    path('',views.home, name = 'home'),
    path('about', views.about , name = 'about'),
    path('signIn',view.signin , name='sign_in'),
    path('logout',view.signout , name ='logout'),  

    #SPECIFIC URLS
]


