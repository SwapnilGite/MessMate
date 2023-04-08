from django.contrib import admin
from django.urls import path,include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.SyMenu,name='syMess'),
    # path('',views.fyMenu,name='fyMess'),
    path('',views.home,name='menu'),
    path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
    # templates\adminstrator\adminlogin.html
    path('studentLogin/',include('student.urls')),
    path('MessAdminLogin/',include('messadmin.urls')),
 
] 
