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

# Create your models here.

class Mess(models.Model):
    
   
    MESS_CHOICES = (
    ("1", "FY"),
    ("2", "SY"),
    ("3", "TY"),
    ("4", "BTech"),
    )
    
    Mess_name = models.CharField(primary_key=True,max_length=50,choices=MESS_CHOICES,default=None)

    def __str__(self):
        return self.Name
    

    
    
    
    