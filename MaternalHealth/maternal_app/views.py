from django.shortcuts import render,redirect
from .forms import PredictionForm
from .models import HealthPrediction,PostNews
import pickle
import numpy as np
import pandas as pd
import xgboost

model=pickle.load(open('./mlModel/classification_model','rb'))
#model=pickle.load(open('classification_model','rb'))

# Create your views here.

def index(request):
    template='maternal_app/maternalrisk/index.html'
    form=PredictionForm()
    post=PostNews.objects.all()
    if request.method=='POST':
        patient_id = request.POST["patient_id"]
        address = request.POST["address"]
        date_of_birth = request.POST["date_of_birth"]
        contact_num = request.POST["contact_num"]
        age_group = request.POST["age_group"]
        systolic_bp = request.POST["systolic_bp"]
        diastolic_bp = request.POST["diastolic_bp"]
        blood_sugar = request.POST["blood_sugar"]
        body_temp = request.POST["body_temp"]
        heart_rate = request.POST["heart_rate"]
        maternal_data=HealthPrediction(patient_id=patient_id,contact_num=contact_num,date_of_birth=date_of_birth,address=address,age_group=age_group,systolic_bp=systolic_bp,diastolic_bp=diastolic_bp,blood_sugar=blood_sugar,body_temp=body_temp,heart_rate=heart_rate)
        maternal_data.save()
        test_data1=[systolic_bp,diastolic_bp,blood_sugar,body_temp,heart_rate,age_group]
        test_data=np.array([test_data1],dtype=float)
        y_predict=model.predict(test_data)
        if y_predict[0]==0:
            y_predict='Low Risk'
        elif y_predict[0]==1:
            y_predict='Medium Risk'
        else:
            y_predict='High Risk'
        print(y_predict)
        form=PredictionForm()
        context={
        'title':'Home',
        'posts':post,     
        'form':form,
        'predict':y_predict
    }
        return render(request,template,context)
    else:
        context={
            'title':'Home',
             'posts':post,   
            'form':form
        }
        return render(request,template,context)

def show(request):
    template='maternal_app/maternalrisk/show.html'
    report=HealthPrediction.objects.all()
    context={
            'title':'Prediction Report',
            'reports':report
        }

    return render(request,template,context)

def edit(request,id):
    template='maternal_app/maternalrisk/edit.html'
    if request.method=='POST':
        data=HealthPrediction.objects.get(pk=id)
        form=PredictionForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=HealthPrediction.objects.get(pk=id)
        form=PredictionForm(instance=data)
    context={
        'form':form,
    }
    return render (request,template,context)

def delete(request,id):
    stu=HealthPrediction.objects.get(id=id).delete()
    return redirect('show')

def news_portal(request,id):
    template='maternal_app/maternalrisk/news.html'
    post=PostNews.objects.filter(id=id)
    context={
        'title':'News ',
        'posts':post
    }
    return render(request,template,context)
    

'''def predi(request):
    age_group=request.GET['age_group']
    systolic_bp=request.GET['systolic_bp']
    diastolic_bp=request.GET['diastolic_bp']
    blood_sugar=request.GET['blood_sugar']
    body_temp=request.GET['body_temp']
    heart_rate=request.GET['heart_rate']
    age_group=request.GET['age_group']

    y_pred=model.predict([[systolic_bp,diastolic_bp,blood_sugar,body_temp,heart_rate,age_group]])

    print(y_pred)'''


    
   
    
