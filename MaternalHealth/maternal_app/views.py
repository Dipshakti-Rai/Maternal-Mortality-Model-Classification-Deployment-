from django.shortcuts import render,redirect
from .forms import PredictionForm
from .models import HealthPrediction,PostNews

# Create your views here.

def index(request):
    template='maternal_app/maternalrisk/index.html'
    form=PredictionForm()
    post=PostNews.objects.all()
    if request.method=='POST':
        form=PredictionForm(request.POST)
        form.save()
        form=PredictionForm()
        context={
        'title':'Home',
        'posts':post,     #News post 
        'form':form
    }
        return render(request,template,context)
    else:
        context={
            'title':'Home',
             'posts':post,     #News post 
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
        #'posts':'post',     #News post 
        'posts':post
    }
    return render(request,template,context)
    

    
   
    
