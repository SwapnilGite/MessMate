from django.db import models

# Create your models here.
from ast import Pass
from asyncio.windows_events import NULL
from curses.ascii import NUL
from datetime import datetime
import email
from email.policy import default
from random import choices
from django.db import models

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
    Mess_name = models.CharField(max_length=50,choices=MESS_CHOICES,default=NULL)
    pass1= models.CharField(max_length=70, default="")
    email=models.EmailField(max_length=100 ,default="")
    
    
    def __str__(self):
        return self.Name
    
    
    