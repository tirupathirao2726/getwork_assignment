from django.shortcuts import render
from .models import Question,Choice
# Create your views here.

def home(request):
    return render(request,'index.html',{})

def get_data(request):
    q=Question.objects.all()
    print(q)
    return render(request,'data.html',{'data':q})
