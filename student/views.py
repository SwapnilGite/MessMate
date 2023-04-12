from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,  login, logout
from student.models import Student
from django.contrib.auth.models import Group
from django.contrib import messages
from administrator.models import Feedback
from datetime import date, timedelta
from messadmin.models import Mess

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
            
            return redirect("studentAfterLogin")
        else:
            return render(request,"student/studentlogin.html")

    return render(request,"student/studentlogin.html")

def studentAfterLogin(request):
    current_user = request.user.username
    print("current_user",current_user)
    current_student=Student.objects.filter(mis=current_user)[0]
    my_dict = {
    "current_student": current_student,
    }
    
    if request.method == "POST":
        if "feedback_form" in request.POST:
            feedback = request.POST.get('feedback', '')
            today_date = date.today()
            Mess_name = current_student.Mess
            Mess_=Mess.objects.filter(Mess_name=Mess_name)[0]
            feed = Feedback.objects.create(feedback=feedback, date=today_date, Mess=Mess_)
            feed.save()
            print("Feedback added")
    return render(request,"student/index.html",my_dict)
            
                


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


def student_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("studentLogin")


