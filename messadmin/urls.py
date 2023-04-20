from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.MessadminLogin,name='MessadminLogin'),
    path('messadminRegister/',views.messadminRegister,name='messadminRegister'),
    path('adminDashboard/',views.adminDashboard,name='adminDashboard'),
    # path('facultyAfterLogin/CreateCourse/',views.CreateCourse,name='CreateCourse'),
    # path('facultyAfterLogin/CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
    # path('facultyAfterLogin/ManageQuiz/',views.ManageQuiz,name='ManageQuiz'),
    # path('facultyAfterLogin/StudentPerformance/',views.StudentPerformance,name='StudentPerformance'),
    path('logout/',views.messadmin_logout,name='logout'),

    # path('studentQuiz',views.studentQuiz,name='studentQuiz'),
]
