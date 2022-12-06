import datetime

from django.shortcuts import render
from f_app.models import  questions

# Create your views here.
def index(request):
    question=questions.objects.all()
    return render(request,'index.html',{"questions":question})

def about(request):
    return render(request,'about.html',{'Name':'RAGT'})

def exam(request):
    message=""

    if request.method=="POST":
        print(request.POST['question'])
        if bool(request.POST['question']) & bool(request.POST['answer']):
            question = questions(question=request.POST['question'],answer=request.POST['answer'],date=datetime.datetime.now())
            question.save()
            message="Add succesfully"
        else:
            message="error check"
    else:
        message=datetime.datetime.now()

    return render(request,'exam.html',{'message':message})