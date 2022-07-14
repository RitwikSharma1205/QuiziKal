
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import *
from django.urls import reverse
from .models import questionTable, quizappUsers
import random
def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('startquiz'))
        else:
            data['error']="username and password are incorrect."
            return render(request,'quizapp/login_page.html',data)
    else:
        return render(request,'quizapp/login_page.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect("http://localhost:8000/quizapp/login-page/")

def signup(request):
    data={}
    if request.method=='POST':
        userdata=User()
        username=request.POST['Username']
        password=request.POST['password']
        email=request.POST['Email']
        if User.objects.filter(username__exact=username) or User.objects.filter(password__exact=password):
            data['error']="username/password already exist"
            return render(request,'quizapp/signup_page.html',data)
        else:
            userdata.username=username
            userdata.set_password(password)
            userdata.email=email
            userdata.save()
            quizuser=quizappUsers()
            quizuser.user=userdata
            quizuser.firstname=request.POST['FirstName']
            quizuser.lastname=request.POST['LastName']
            quizuser.save()
            return  HttpResponseRedirect("http://localhost:8000/quizapp/login-page/")
    return render(request,'quizapp/signup_page.html',data)

def instructions(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/quizapp/login-page/")
    return render(request,'quizapp/instruction_page.html')

def showQuiz(request):
    if 'username' in request.session:
        s=set()
        data={}
        que=questionTable.objects.all()
        while(len(s)<10):
            s.add(random.randint(1,que.count()))
            request.session['QuestionIDs']=list(s)
            q=[]
            for i in s:
                q.append(que.get(id=i))
            data['q']=q
        return render(request,'quizapp/quiz_page.html',data)
    else:
        return HttpResponseRedirect("http://localhost:8000/quizapp/login-page/")
def showResult(request):
    if 'username' in request.session:
        if request.method=='POST':
            formData=request.POST
            total=0
            correct=0
            incorrect=0
            for i in request.session['QuestionIDs']:
                q=questionTable.objects.get(id=i)
                if formData[str(i)]==q.answer:
                    correct+=1
                    total+=2
                else:
                    incorrect+=1
            data={
                'total':total,
                'correct':correct,
                'incorrect':incorrect
            }
            return render(request,'quizapp/result_page.html',data)
        else:
            return HttpResponseRedirect("http://localhost:8000/quizapp/Instructions/")
    else:
        return HttpResponseRedirect("http://localhost:8000/quizapp/login-page/")
