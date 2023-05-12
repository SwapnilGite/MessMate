from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate,  login, logout
from messadmin.models import MessAdmin
from messadmin.models import Menu
from administrator.models import Mess
from messadmin.models import MealRecord
from django.contrib.auth.models import Group
import datetime
from datetime import date
from student.models import Student
from administrator.models import Feedback
from administrator.models import Transaction

from datetime import datetime, timedelta
from messadmin.models import BfRecord
from messadmin.models import Bill

def MessadminLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("adminDashboard")
        else:
            return render(request,"messadmin/mess_adminlogin.html")

    return render(request,"messadmin/mess_adminlogin.html")

def adminDashboard(request):
    
    admin_id=request.user.username
    mess_admin=MessAdmin.objects.filter(Admin_id=admin_id)[0]
    messAdminName = mess_admin.Name
    Mess_=mess_admin.Mess.Mess_name
    all_students=Student.objects.filter(Mess=Mess_)
    print(all_students)
 
    
    
    today_menu=Menu.objects.filter(Mess=Mess_)[0]
  


        
    print("dffd",today_menu.Breakfast)
    
    all_feedbacks=Feedback.objects.filter(Mess=mess_admin.Mess);
    for feedback in all_feedbacks:
        print(feedback.feedback)
    my_dict = {"messAdminName":messAdminName,
    "all_students": all_students,
    "all_feedback":all_feedbacks,
    "today_menu" : today_menu,
    }
    # print("Fdd")increase_count update_menu
    
  
        
    if request.method == "POST":
        print("Ïnserted")
        print(request.POST)
        if "increase_count" in request.POST:
            print("increase_count")
            student_mis = request.POST.get('student')
            print(student_mis)
            student = Student.objects.filter(mis=student_mis)[0]
            admin_id=request.user.username
            mess_admin=MessAdmin.objects.filter(Admin_id=admin_id)[0]
            Mess_=mess_admin.Mess
            today_date = date.today()
            current_month = today_date.strftime("%B")
            print("month")
            print(current_month)
            # check if a meal record for this student and month already exists
            try:
                meal_record = MealRecord.objects.get(Student=student, month=current_month)
                meal_record.Messname=Mess_
                meal_record.mealcount += 1
                meal_record.Messname=Mess_
                meal_record.Student=student
                meal_record.save()
                message = f"Meal count for {student.Name} increased to {meal_record.mealcount} for {current_month}"
                print(message)
            except MealRecord.DoesNotExist:
                meal_record = MealRecord.objects.create(Student=student,month=current_month,Messname=Mess_)
                meal_record.save()
                meal_record.save()
                message = f"Meal count for {student.Name} set to 1 for {current_month}"
                print(message)
            
            try:     
                # bf_record = BfRecord.objects.get(Student=student, month=current_month)
                # meal_record = MealRecord.objects.get(Student=student, month=current_month)
                
                bill_record = Bill.objects.get(Student_id=student)
                # bill_record.total_bill=bf_record.amount+40*(meal_record.mealcount)
                bill_record.total_bill=bill_record.total_bill+40
                
                bill_record.month=current_month
                bill_record.save()
                
            except Bill.DoesNotExist:
                # bf_record = BfRecord.objects.get(Student=student, month=current_month)
                # meal_record = MealRecord.objects.get(Student=student, month=current_month)
                
                bill_record = Bill.objects.create(Student_id=student,month=current_month)
                bill_record.total_bill=bill_record.total_bill+40
                bill_record.save()
                
            return render(request, 'messadmin/mess_admindash.html',my_dict)
        
        if "update_menu" in request.POST:
            print("update_menu")
            current_user = request.user.username
        
            admin = MessAdmin.objects.get(Admin_id=current_user)
            Mess = admin.Mess

            # get the menu data from the POST request
            breakfast = request.POST.get('Breakfast', '')
            veg_lunch = request.POST.get('VegLunch', '')
            non_veg_lunch = request.POST.get('NonVegLunch', '')
            veg_dinner = request.POST.get('VegDinner', '')  # fixed variable name
            non_veg_dinner = request.POST.get('NonVegDinner', '') # fixed variable name
            eve_snacks = request.POST.get("EveSnacks", '')

            # get the current date
            today = date.today()

            # check if a Menu object already exists for this Mess and date
            try:
                menu = Menu.objects.get(Mess=Mess)
            except Menu.DoesNotExist:
                # if no Menu object exists, create a new one and save it
                menu = Menu(Mess=Mess, Breakfast=breakfast, VegLunch=veg_lunch, NonVegLunch=non_veg_lunch, VegDinner=veg_dinner, NonVegDinner=non_veg_dinner, EveSnacks=eve_snacks, date=today)
                menu.save()
                print("New menu created")
            else:
                # if a Menu object already exists, update it
                menu.Breakfast = breakfast
                menu.VegLunch = veg_lunch
                menu.NonVegLunch = non_veg_lunch
                menu.VegDinner = veg_dinner
                menu.NonVegDinner = non_veg_dinner
                menu.EveSnacks = eve_snacks
                menu.save()
                print("Menu updated")
                
            return redirect('adminDashboard')
        
        if "add_breakfast" in request.POST:
            student_mis = request.POST.get('student')
            student = Student.objects.filter(mis=student_mis)[0]
            print("student ",student.Name)
            admin_id=request.user.username
            mess_admin=MessAdmin.objects.filter(Admin_id=admin_id)[0]
            Mess_=mess_admin.Mess
            # get the current date
            today = date.today()

            current_month = today.strftime("%B")
            
            breakfast=request.POST.getlist('breakfast[]')
            breakfast_bill=0;
            for i in breakfast: 
                if i=='tea':
                    breakfast_bill+=11
                if i=="code-milk":
                    breakfast_bill+=20
                if i=="born-vita":
                    breakfast_bill+=20
                    
                if i=="biscuits":
                    breakfast_bill+=5
                print("breakfast_bill",breakfast_bill)
            try:
                bf_record = BfRecord.objects.get(Student=student, month=current_month)
                bf_record.Messname=Mess_
                bf_record.amount += breakfast_bill
                bf_record.Messname=Mess_
                bf_record.Student=student
                bf_record.save()
                message =  f" Current breakfast for {student.Name}  for {current_month} is {bf_record.amount}"
                print(message)
            except BfRecord.DoesNotExist:
                bf_record = BfRecord.objects.create(Student=student,month=current_month,Messname=Mess_,amount=breakfast_bill)
                bf_record.save()
                message = f" new : Current breakfast for {student.Name}  for {current_month} is {bf_record.amount}"
                print(message)
                
            try:     
                # bf_record = BfRecord.objects.get(Student=student, month=current_month)
                # meal_record = MealRecord.objects.get(Student=student, month=current_month)
                
                bill_record = Bill.objects.get(Student_id=student)
                # bill_record.total_bill=bf_record.amount+40*(meal_record.mealcount)
                bill_record.total_bill=bill_record.total_bill+breakfast_bill                
                bill_record.month=current_month
                bill_record.save()
                
            except Bill.DoesNotExist:
                # bf_record = BfRecord.objects.get(Student=student, month=current_month)
                # meal_record = MealRecord.objects.get(Student=student, month=current_month)
                
                bill_record = Bill.objects.create(Student_id=student,month=current_month)
                bill_record.total_bill=bill_record.total_bill+breakfast_bill
                bill_record.save()
          
            
    return render(request, "messadmin/mess_admindash.html",my_dict)


def messadminRegister(request):
      
    if request.method=="POST":
        Admin_id=request.POST.get('Admin_id','')
        Name=request.POST.get('Name', '')
        Mess_name=request.POST.get("Mess_name",'')
        pass1=request.POST.get('pass1','')
        email=request.POST.get('email', '')
        
        Mess_=Mess.objects.filter(Mess_name=Mess_name)[0]
        print(Mess_)
        print("Admin_id : ",Admin_id)
        print("Name : ",Name)
        print("Mess_name : ",Mess_name)
        print("pass1 : ",pass1)
        print("email : ",email)
        
        MessAd =MessAdmin(Admin_id=Admin_id,Name=Name,Mess=Mess_,pass1=pass1,email=email)
        MessAd.save()
        
        
        # Create the user
        myuser = User.objects.create_user(Admin_id, email, pass1)
        myuser.save()
        my_group = Group.objects.get(name='messadmin') 
        my_group.user_set.add(myuser)

        return render(request,"messadmin/mess_adminregister.html")   
        
        # return redirect('studenthome')
    else:
        return render(request,"messadmin/mess_adminregister.html")   

def tranHistory(request):
    admin_id=request.user.username
    mess_admin=MessAdmin.objects.get(Admin_id=admin_id)
    Mess_=mess_admin.Mess.Mess_name
    all_students=Student.objects.filter(Mess=Mess_)
    all_transactions=Transaction.objects.filter()
    all_transactionss=[]
    for transaction in all_transactions:
        if(transaction.Student_id.Mess==Mess_):
            all_transactionss.append(transaction)
    my_dict = {
    "all_students": all_students,
    "all_transactions":all_transactionss,
    "months":["January","February","March","April","May","June","July","August","September","October","November","December"]}
    
    return render(request,"messadmin/transaction.html",my_dict)


def messadmin_logout(request):
    logout(request)
    return redirect(MessadminLogin)