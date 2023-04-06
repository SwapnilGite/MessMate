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
# Create your models here.

class MessAdmin(models.Model):
    
   
    MESS_CHOICES = (
    ("1", "FY"),
    ("2", "SY"),
    ("3", "TY"),
    ("4", "BTech"),
    )
    
    Admin_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Mess_name = models.ForeignKey(Mess,on_delete=models.CASCADE)
    pass1= models.CharField(max_length=70, default="")
    email=models.EmailField(max_length=100 ,default="")
    
    
    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    
    Messname = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    Brekfast = models.CharField(max_length=50)
    VegLunch = models.CharField(max_length=50,default=None)
    NonVegLunch = models.CharField(max_length=50,default=None)
    Dinner = models.CharField(max_length=50,default=None)
    NonVegDinner = models.CharField(max_length=50,default=None)
    EveSnacks = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.Name
    
    
class MealRecord(models.Model):
    
    Meal_id = models.IntegerField(primary_key=True, auto_created=True)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
    Messname = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    mealcount = models.IntegerField(default=0);
    
    # Messname = models.ForeignKey(Mess,on_delete=models.CASCADE,default=None);
    # Brekfast = models.CharField(max_length=50)
    # VegLunch = models.CharField(max_length=50,default=None)
    # NonVegLunch = models.CharField(max_length=50,default=None)
    # Dinner = models.CharField(max_length=50,default=None)
    # NonVegDinner = models.CharField(max_length=50,default=None)
    # EveSnacks = models.CharField(max_length=50)
    # Notes=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
    
