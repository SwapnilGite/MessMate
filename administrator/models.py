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

# from messadmin.models import Mess
# Create your models here.

class Mess(models.Model):
    MESS_CHOICES = (
    ("FY", "FY"),
    ("SY", "SY"),
    ("TY", "TY"),
    ("BTech", "BTech"),
    )
    
    Mess_name = models.CharField(primary_key=True,max_length=50,choices=MESS_CHOICES,default=None)

    def __str__(self):
        return self.Mess_name
    
class Feedback(models.Model):
    feedback = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    Mess=models.ForeignKey(Mess,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return str(self.date)
