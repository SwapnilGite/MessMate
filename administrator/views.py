from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout
from messadmin.models import Mess
from messadmin.models import Menu
from django.template import loader
from django.utils import timezone
from datetime import date,timedelta


def home(request):
    
    dict={}
    try:
        fymenu=Menu.objects.filter(Mess='FY',date=date.today())[0]
    except:
        fymenu=Menu.objects.filter(Mess='FY',date=date.today()-timedelta(days=1))[0]
        
    try:
        symenu=Menu.objects.filter(Mess='SY',date=date.today())[0]
    except:
        symenu=Menu.objects.filter(Mess='SY',date=date.today()-timedelta(days=1))[0]
        
    try:
        tymenu=Menu.objects.filter(Mess='TY',date=date.today())[0]
    except:
        tymenu=Menu.objects.filter(Mess='TY',date=date.today()-timedelta(days=1))[0]
        
    try:
        btechmenu=Menu.objects.filter(Mess='BTech',date=date.today())[0]
    except:
        btechmenu=Menu.objects.filter(Mess='BTech',date=date.today()-timedelta(days=1))[0]
  
    
    print(fymenu)
    print(symenu)
    print(tymenu)
    print(btechmenu)
    my_dict = {
    "fymenu": fymenu,
    "symenu": symenu,
    "tymenu": tymenu,
    "btechmenu": btechmenu
}
    
    print(my_dict['fymenu']);
    # FY_MENU=
    return render(request,'administrator/index.html',my_dict)

def AdminLogin(request):
    # return HttpResponse("Admin Login Entered")
    return render(request,'administrator/adminlogin.html')
    # return render(request,'administrator/index.html')
    
    # if request.method=="POST":
        
    #     loginusername=request.POST['loginusername']
    #     loginpassword=request.POST['loginpassword']
    #     loginemail=request.POST['loginemail']
        
    #     # print("loginusername : ",loginusername)
    #     # print("loginpassword : ",loginpassword)
        
    #     user=authenticate(username= loginusername, password= loginpassword)
    #     if user is not None and request.user.is_superuser:
    #         login(request, user)
    #         return HttpResponse("Superuser Logged In")
    #         # return render(request,"admin/adminLogin.html")
    #     else:
    #         # loginstatus={"valid":0}
    #         # return render(request,"student/home.html",loginstatus)
    #         return HttpResponse("You are not allowed to visit this page")
    
    # return render(request,"administrator/adminlogin.html")
