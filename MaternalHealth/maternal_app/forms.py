from tkinter import Widget
from django import forms
from django import forms
from .models import HealthPrediction

class PredictionForm(forms.ModelForm):
    
    class Meta:
        model = HealthPrediction
        fields = '__all__'
        labels={'patient_id':'Patient ID','address':'Address','date_of_birth':'Date of Birth',
        'contact_num':'Contact','age_group':'Age Group','systolic_bp':'Systolic Blood Pressure',
        'diastolic_bp':'Diastolic Blood Pressure','blood_sugar':'Blood Sugar','body_temp':'Body Temperature'

        }
        widgets={
            'patient_id':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control'}),
            'contact_num':forms.NumberInput(attrs={'class':'form-control'}),
            'age_group':forms.NumberInput(attrs={'class':'form-control'}),
            'systolic_bp':forms.NumberInput(attrs={'class':'form-control'}),
            'diastolic_bp':forms.NumberInput(attrs={'class':'form-control'}),
            'blood_sugar':forms.NumberInput(attrs={'class':'form-control'}),
            'body_temp':forms.NumberInput(attrs={'class':'form-control'})
        }