from django.db import models

# Create your models here.
from ast import Pass
# from asyncio.windows_events import NULL
from curses.ascii import NUL
from datetime import datetime
import email
from email.policy import default
from random import choices
from django.db import models
from administrator.models import Mess
from django.utils import timezone
from student.models import Student
# from messadmin.models import BfRecord
# Create your models here.

class MessAdmin(models.Model):
    
   
    MESS_CHOICES = (
    ("FY", "FY"),
    ("SY", "SY"),
    ("TY", "TY"),
    ("BTech", "BTech"),
    )
    
    Admin_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Mess = models.ForeignKey(Mess,on_delete=models.CASCADE)
    pass1= models.CharField(max_length=70, default="")
    email=models.EmailField(max_length=100 ,default="")
    
    
    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    
    Mess = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    Breakfast = models.CharField(max_length=50)
    VegLunch = models.CharField(max_length=50,default=None)
    NonVegLunch = models.CharField(max_length=50,default=None)
    VegDinner = models.CharField(max_length=50,default=None)
    NonVegDinner = models.CharField(max_length=50,default=None)
    EveSnacks = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Mess.Mess_name+" "+str(self.date)
    
    
class MealRecord(models.Model):
    
    months = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
    )
    
   
    Meal_id = models.AutoField(primary_key=True)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
    Messname = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    mealcount = models.IntegerField(default=1);
    month = models.CharField(max_length=50,choices=months,default=None)
    
    def __str__(self):
        return str(self.Student.Name)+" "+str(self.month)
class BfRecord(models.Model):
    
    months = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
    )
    
   
    Bf_id = models.AutoField(primary_key=True)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
    Messname = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    amount = models.IntegerField(default=0);
    month = models.CharField(max_length=50,choices=months,default=None)
    
    def __str__(self):
        return str(self.Student.Name)+" "+str(self.month)
    
class Bill(models.Model):
    # billpaid=(
    #     ('0','0'),
    #     ('1','1')
    # )
    
    months = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
    )
    
    Bill_id=models.AutoField(primary_key=True)
    Meal_id=models.ForeignKey(MealRecord,default=None,on_delete=models.CASCADE)
    Bf_id=models.ForeignKey(BfRecord,default=None,on_delete=models.CASCADE)
    total_bill=models.IntegerField(default=0);
    bill_paid=models.IntegerField(default=0);
    month = models.CharField(max_length=50,choices=months,default=None)

    def __str__(self):
        return self.Bill_id