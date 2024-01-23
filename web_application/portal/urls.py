from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard , name ='dashboard'),  
    path('networkPrediction',views.NetworkPrediction , name ='Prediction'),  
    path('networkPerfomance',views.NetworkPerfomance , name ='Perfomance'), 

    #URLS FOR FEED BACK 
    path('AddCompain_Feedback',views.AddFedComp , name ='addFed'),
    path('View_Complains',views.ViewFedComp , name ='ViewComp'),  
     path('recomandations',views.Recomandation , name ='recomandation'), 
    path('updateuotation/<int:pk>',views.updateFedComp, name = 'UpdateE36'),  
]


