from ast import Pass
# from asyncio.windows_events import NULL
from curses.ascii import NUL
from datetime import datetime
import email
from email.policy import default
from random import choices
from django.db import models
# from messadmin.models import Mess
# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
    )
    
    YEAR_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    )
    MESS_CHOICES = (
    ("FY", "FY"),
    ("SY", "SY"),
    ("TY", "TY"),
    ("BTech", "BTech"),
    )
    
    mis = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default=None)
    Year=models.IntegerField(choices=YEAR_CHOICES)
    Dept = models.CharField(max_length=70, default="")
    Mess=models.CharField(max_length=20,choices=MESS_CHOICES,default="")
    pass1= models.CharField(max_length=70, default="")
    email=models.EmailField(max_length=100 ,default="")
    
    
    def __str__(self):
        return self.Name
    

# class M




