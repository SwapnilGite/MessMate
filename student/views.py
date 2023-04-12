from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,  login, logout
from student.models import Student
from django.contrib.auth.models import Group
from django.contrib import messages
# from quiz.models import Quiz
# from quiz.models import Result
# from quiz.models import Question
import datetime
quiz_dict={}
Quiz_dict={}


def studentLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            print("Hello World\n");
            login(request, user)
            # return HttpResponse("Student Login\n");
            return redirect("studentAfterLogin")
        else:
            # loginstatus={"valid":0}
            # return render(request,"student/studentlogin.html",loginstatus)
            return render(request,"student/studentlogin.html")

    return render(request,"student/studentlogin.html")

def studentRegister(request):
       
    if request.method=="POST":
        Name=request.POST.get('Name', '')
        Gender=request.POST.get("Gender",'')
        Year=request.POST.get("Year",'')
        mis=request.POST.get('MIS','')
        MessEnrolled=request.POST.get('MESS_ENR','')
        Dept=request.POST.get('Dept','')
        pass1=request.POST.get('pass1','')
        email=request.POST.get('email', '')
        
    
        student =Student(Name=Name,mis=mis,Gender=Gender,Mess=MessEnrolled,pass1=pass1,Year=Year,Dept=Dept,email=email)
        student.save()
        
        print("Name : ",Name)
        print("Gender : ",Gender)
        print("Year : ",Year)
        print("mis : ",mis)
        print("Dept : ",Dept)
        print("Mess : ",MessEnrolled)
        print("pass1 : ",pass1)
        print("email : ",email)
        
        
        # Create the user
        myuser = User.objects.create_user(mis, email, pass1)
        myuser.save()
        my_group = Group.objects.get(name='student') 
        my_group.user_set.add(myuser)

        return redirect("studentLogin") 
        
        # return redirect('studenthome')
    else:
        return render(request, "student/studentregister.html")

def studentAfterLogin(request):
    return render(request,"student/studentAfterLogin.html");


