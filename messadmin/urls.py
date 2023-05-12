from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.MessadminLogin,name='MessadminLogin'),
    path('messadminRegister/',views.messadminRegister,name='messadminRegister'),
    path('adminDashboard/',views.adminDashboard,name='adminDashboard'),
    path('tranHistory/',views.tranHistory,name='tranHistory'),
    path('logout/',views.messadmin_logout,name='logout'),
]
