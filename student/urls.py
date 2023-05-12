from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.studentLogin,name='studentLogin'),
    path('studentRegister/',views.studentRegister,name='studentRegister'),
    path('studentAfterLogin/',views.studentAfterLogin,name='studentAfterLogin'),
    path('student_logout/',views.student_logout,name='student_logout'),
  
]
