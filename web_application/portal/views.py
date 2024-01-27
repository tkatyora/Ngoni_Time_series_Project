from django.shortcuts import render, redirect
from account.models import *
from .models import Feedback_Complains
from django.contrib.auth.decorators import login_required
import csv
import pandas as pd
import matplotlib.pyplot as plt
from .forms import Feedback_ComplainsForm
from django.contrib import messages
# Create your views here.
users = NetworkProfile.objects.all().filter()
fedcomp = Feedback_Complains.objects.all()
@login_required(login_url='sign_in')
def dashboard(request):
    content ={}
    content = {
        'networkuser':users
   
    }  
    return render(request , 'Portal/mainDashboard.html',content)

#--------------------------------CRUD OPERATIONS FOR NETWORK PERFOMANCE---------------------------------------------
#1.1 DIsplaying all Network Statistics

@login_required(login_url='sign_in')
def NetworkPerfomance(request):
    newdata_set = pd.read_csv('PredictionModel/NetworkFalure.csv')
    ip = request.GET.get('ip',None)
    
    date = request.GET.get('date',None)
    #Plotting for specific customeer
    df_customer = newdata_set.loc[newdata_set['Destination.IP'] == ip]
    df_Ratio = df_customer['Down.Up.Ratio']
    df_time = df_customer['Date']
    plt.plot(df_Ratio,df_time)
    plt.title('DownUp Ratio for the whole network')
    plt.xlabel('Date')
    plt.ylabel('DownUp Ratio')
    plt.savefig('static/Images/Prediction/updowns.png')
    data = plt.show()
   
    content ={}
    content ={
        'stats': users,
        'ip':ip,
        'date':df_customer,
        'img': data
    }  
    return render(request , 'Portal/Perfomance.html',content)

#--------------------------------CRUD FOR FAILURE PREDICTION-------------------------------------------
@login_required(login_url='sign_in')
def NetworkPrediction(request):
    newdata_set = pd.read_csv('PredictionModel/prediction.csv')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Network Prediction')
    newdata_set.plot(color='red', linestyle='--')
    prediction =plt.show()
    # with open(prediction, 'r') as f:
    #     reader = csv.reader(f)
    #     data = reader
    content ={}
    content ={
        'predictions':prediction,
        'recomand': users
   
    }  
    return render(request , 'Portal/Prediction.html',content)



#------------------       Code Block Responsible for CRUD OPERATIONS Of Complains and Feedbacks--------------------------------------- 
#3.1 CREATING FEDCOMP
@login_required(login_url='sign_in')
def AddFedComp(request):
    if request.method == 'POST':
        form = Feedback_ComplainsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            fedcomp = form.save(commit=False)
            fedcomp.created_by = request.user
            fedcomp.save()
            form.save()
            mesage= f'Fedback added succesfully'
            messages.success(request,mesage)
            return redirect('addFed')   
        else:
            messages.warning(request, 'Sorry Feedback not added succesfully')
    else:
        form = Feedback_ComplainsForm()
    content = {}
    content = {
        'form': form,

    }  
    return render(request , 'Portal/AddFedComp.html',content)

#3.2 VIEWFEDCOMP (READ)
@login_required(login_url='sign_in')
def ViewFedComp(request):
    content ={}
    content ={
        'fedcomp': fedcomp,
    
    }  
    return render(request , 'Portal/ViewComp.html',content)

#3.3 REPLYCOMP
@login_required(login_url='sign_in') 
def replyComp(request, pk):
    reply = Feedback_Complains.objects.get(id=pk)  
    if request.method == 'POST':
        form = Feedback_ComplainsForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reply updated succesfully')
            return redirect('dashboard')
            
        else:
            messages.warning(request, 'Sorry Reply Failled')
    else:
        form = Feedback_ComplainsForm(instance=reply)
    content = {}
    content = {
        'form':  form,
        'reply': reply

    }
    return render(request, 'Portal/reply.html', content)



#---------------------------------------------------CODE FOR RECOMANDATIONS---------------------------------------

#4.1 READ 
@login_required(login_url='sign_in')
def Recomandation(request):
    content ={}
    content ={
        'recomand': users
    }  
    return render(request , 'Portal/recomandation.html',content)
