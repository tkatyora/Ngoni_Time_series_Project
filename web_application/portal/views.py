from django.shortcuts import render, redirect
from account.models import *
from .models import Feedback_Complains
from django.contrib.auth.decorators import login_required
import csv
import pandas as pd
import matplotlib.pyplot as plt
from .forms import Feedback_ComplainsForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site



# Create your views here.
users = NetworkProfile.objects.all().filter()
fedcomp = Feedback_Complains.objects.all().order_by('-updated')
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
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read the DataFrame
    df_predict = pd.read_csv('PredictionModel/NetworkFalure.csv')

    # Get request parameters
    ip = request.GET.get('ip', None)
    date = request.GET.get('date', None)
    starttime = request.GET.get('starttime', None)
    endtime = request.GET.get('endtime', None)

    # Filter the DataFrame for specific customer and time range
    df_display = df_predict[(df_predict['Date'] == date)]
    df_predict = df_display[(df_display['Time'] >= starttime) & (df_display['Time'] <= endtime)]
    df_customer = df_predict[df_predict['Destination.IP'] == ip]

    # Create subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    # Plot DownUp Ratio
    axs[0].plot(df_customer['Time'], df_customer['Down.Up.Ratio'])
    axs[0].set_title('Graph for Down Up Ratio')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('DownUp Ratio')
    axs[0].tick_params(axis='x', rotation=85)

    # Plot ACK
    axs[1].plot(df_customer['Time'], df_customer['ACK.Flag.Count'])
    axs[1].set_title('ACKAcknowledgement Graph')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Acknowledgement Flag')
    axs[1].tick_params(axis='x', rotation=85)
    plt.tight_layout()
    # Save figures
    plt.savefig('static/Images/Prediction/updowns_ack.png')
    plt.close()

    content = {
        'stats': users,
        'ip': ip,
        'date': date,
        'starttime': starttime,
        'endtime': endtime
    }

    return render(request, 'Portal/Perfomance.html', content)


@login_required(login_url='sign_in')
def NetworkPerfomanceWhole(request):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read the DataFrame
    df_predict = pd.read_csv('PredictionModel/NetworkFalure.csv')
    date = request.GET.get('date_whole', None)
    starttime = request.GET.get('starttime_whole', None)
    endtime = request.GET.get('endtime_whole', None)
    print(date)
    
    # Filter the DataFrame for specific date and time range
    
    df_display = df_predict[(df_predict['Date'] == date)]
    df_display2 = df_display[(df_display['Time'] >= starttime) & (df_display['Time'] <= endtime)]
    
    # Extract relevant data
    df_Ratio = df_display2['Down.Up.Ratio']
    df_time = df_display2['Time']
    df_ack = df_display2['ACK.Flag.Count']

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot for the first subplot (DownUp Ratio)
    ax1.plot(df_time, df_Ratio)
    ax1.set_title('DownUp Ratio for the whole network')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('DownUp Ratio')
    ax1.tick_params(axis='x', rotation=85)

    # Plot for the second subplot (ACK Flag)
    ax2.plot(df_time, df_ack)
    ax2.set_title('Ack Flag for the whole network')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Acknowledgement Flag')
    ax2.tick_params(axis='x', rotation=85)

    # Adjust layout
    plt.tight_layout()

    # Save figures
    plt.savefig('static/Images/Prediction/Wholeupdowns_ack.png')
    plt.close()

    content = {
        'stats': users,
        'date': date,
        'starttime': starttime,
        'endtime': endtime
    }

    return render(request, 'Portal/PerfomanceWhole.html', content)


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



#---------------------- CRUD OPERATIONS Of Complains and Feedbacks--------------------------------------- 
#3.1 CREATING FEDCOMP
@login_required(login_url='sign_in')
def AddFedComp(request):
    if request.method == 'POST':
        form = Feedback_ComplainsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            types = form.cleaned_data['type']
            fedcomp = form.save(commit=False)
            fedcomp.created_by = request.user
            fedcomp.save()
            print('this is a ',types)
            form.save()
            if types == 'Complain':
                mesage= f'Complain added succesfully'
            else:
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
    print('creatdby',reply.created_by) 
    if request.method == 'POST':
        form = Feedback_ComplainsForm(request.POST, instance=reply)
        if form.is_valid():
            fedcomp = form.save(commit=False)
            fedcomp.created_by = reply.created_by
            fedcomp.save()
            messages.success(request, 'Reply created succesfully')
            
            
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

#---------------------------------------------------CLIENTS MANAGEMENT---------------------------------------------
@login_required(login_url='sign_in')
def View_Clients(request):
    domain = get_current_site(request).domain
    content ={}
    content ={
        'recomand': users,
        'domain':domain
    }  
    return render(request , 'Portal/view_client.html',content)
