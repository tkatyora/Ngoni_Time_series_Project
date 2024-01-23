from django import forms
from django.forms import ModelForm 
from .models import * 



class Feedback_ComplainsForm(ModelForm):
    type =forms.ChoiceField(choices=Feedback_Complains.Type, label='Select Complain or Feebback',required=True)
    body =forms.CharField(label='Write Comments Complain or Feedback', required=False, help_text='Write Complain or Feedback) ',
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':3,
                                      'cols':3, 
                                  }
                              ))
    reply =forms.CharField(label='Write Reply', required=False, help_text='Write Anything related to the e36(optional) ',
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':3,
                                      'cols':3, 
                                  }
                              ))
 
   

    class Meta: 
        model = Feedback_Complains
        fields =['type','body','created_by','reply']
        
        
    

