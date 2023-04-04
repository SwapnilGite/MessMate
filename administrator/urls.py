from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
    # templates\adminstrator\adminlogin.html
    # path('studentLogin/',include('student.urls')),
    # path('FacultyLogin/',include('faculty.urls')),
]
