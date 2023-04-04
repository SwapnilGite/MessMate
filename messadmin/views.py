from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate,  login, logout
from messadmin.models import MessAdmin
from django.contrib.auth.models import Group
# from quiz.models import Course
# from quiz.models import Quiz
# from quiz.models import Question
# from quiz.models import Result
# from faculty.models import Faculty

def MessadminLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect(facultyAfterLogin)
        else:
            
            return render(request,"messadmin/mess_adminlogin.html")

    return render(request,"messadmin/mess_adminlogin.html")

def messadminRegister(request):
   
    if request.method=="POST":
        Admin_id=request.POST.get('Admin_id','')
        Name=request.POST.get('First_Name', '')
        Mess_name=request.POST.get("Mess_name",'')
        pass1=request.POST.get('pass1','')
        email=request.POST.get('email', '')
        
        MessAd =MessAdmin(Admin_id=Admin_id,Name=Name,Mess_name=Mess_name,pass1=pass1,email=email)
        MessAd.save()
        
        print("Admin_id : ",Admin_id)
        print("Name : ",Name)
        print("Mess_name : ",Mess_name)
        print("pass1 : ",pass1)
        print("email : ",email)
        
        
        # Create the user
        myuser = User.objects.create_user(Admin_id, email, pass1)
        myuser.save()
        my_group = Group.objects.get(name='messadmin') 
        my_group.user_set.add(myuser)

        return render(request,"messadmin/mess_adminregister.html")   
        
        # return redirect('studenthome')
    else:
        return render(request,"messadmin/mess_adminregister.html")   

# def facultyAfterLogin(request):
#     return render(request,"faculty/facultyAfterlogin.html")



# def CreateCourse(request):
    
#     # return render(request,"faculty/createCourse.html")
#     if request.method=="POST":
#         Course_name=request.POST.get('Course_name', '')
#         Course_dept=request.POST.get('Course_dept', '')
#         Credit=request.POST.get("Credit",'') 
        
#         # print("Course_Name : ",Course_name)
#         # print("Department : ",Course_dept)
#         # print("Credit : ",Credit)
#         course =Course(Course_name=Course_name,Course_dept=Course_dept,Credit=Credit)
#         course.save()
        
    
#         return render(request,"faculty/createCourse.html")   
#     else:
#         return render(request, "faculty/createCourse.html")
    
    
#     #  class Quiz(models.Model):
    
#     #     Quiz_id=models.AutoField(primary_key=True)
#     #     Quiz_name=models.CharField(max_length=100)
#     #     Quiz_Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
#     #     Quiz_Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
#     #     date=models.DateField(default=datetime.now)
#     #     def __str__(self):
#     #         return self.Quiz_name 
    
# def CreateQuiz(request):
    
#     # return render(request,"faculty/createCourse.html")
#     if request.method=="POST":
#         Quiz_name=request.POST.get('Quiz_name', '')
#         Courses=request.POST.get('Course_name', '')
#         date=request.POST.get("date",'') 
        
#         Quiz_Course_id=Course.objects.filter(Course_name=Courses)[0]
#         Curr_User=request.user
        
#         Quiz_Faculty=Faculty.objects.filter(email=Curr_User)[0]

#         quiz=Quiz(Quiz_name=Quiz_name,Quiz_Course_id=Quiz_Course_id,Quiz_Faculty=Quiz_Faculty,date=date)
#         quiz.save()
#         return render(request,"faculty/CreateQuiz.html")   
#     else:
#         return render(request, "faculty/CreateQuiz.html")
    
# def StudentPerformance(request):
#     components={}
#     curruser=request.user
#     currfaculty=Faculty.objects.filter(email=curruser.username).first()
#     resultslist=[]
#     resultsname=[]
#     allQuizzes=Quiz.objects.filter(Quiz_Faculty=currfaculty)
#     components["quizzes"]=allQuizzes
#     if request.method == "POST":
#         selected_quiz=request.POST.get("selected_quiz",'')
#         print("selected quizz is",selected_quiz)
#         quizz=Quiz.objects.filter(Quiz_Faculty=currfaculty,Quiz_name=selected_quiz).first()
#         results=Result.objects.filter(Quiz=quizz).order_by('-marks')
#         components["selected_quiz"]=selected_quiz
#         components["results"]=results

#         return render(request,"faculty/StudentPerformance.html",components)
#     else:
#         return render(request,"faculty/StudentPerformance.html",components)

#     # for quizz in quizzes:
#     #     print(quizz)
#     #     results=Result.objects.filter(Quiz=quizz).order_by('-marks')
#     #     resultslist.append(results)
#     #     resultsname.append(quizz.Quiz_name)
#     # # components["resultslist"]=resultslist
#     # # components["quizzes"]=quizzes
#     # # components["resultsname"]=resultsname
#     # return render(request,"faculty/StudentPerformance.html",components)

# # class Quiz(models.Model):
    
# #     Quiz_id=models.AutoField(primary_key=True)
# #     Quiz_name=models.CharField(max_length=100)
# #     Quiz_Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
# #     Quiz_Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
# #     date=models.DateField(default=datetime.now)
# #     def __str__(self):
# #         return self.Quiz_name



# dict={"flag":0}
# def ManageQuiz(request):
    
#     if 'submit1' in request.POST:
#         Quiz_name=request.POST.get('Quiz_name', '')
#         Total_Questions=request.POST.get('Total_Questions', '')
        
#         list=[]
#         for i in range(int(Total_Questions)):
#             list.append(i)
        
#         dict["Quiz_name"]=Quiz_name
#         dict["Total_Questions"]=Total_Questions
#         dict["flag"]=1
#         dict["list"]=list
        
#         Quiz_Course_id=Quiz.objects.filter(Quiz_name=Quiz_name).first()
#         dict["Quiz_Course_id"]=Quiz_Course_id
        
#         return render(request, "faculty/ManageQuiz.html",dict)
    
#     if 'submit2' in request.POST:
#         # Question-{{forloop.counter}}
#         # return HttpResponse("submit2 here") 
#         print("Enter in submit 2")
#         print(dict["Total_Questions"])
#         for i in range(int(dict["Total_Questions"])):
#             print("Question-"+str(i+1))
#             Question_quiz=dict["Quiz_Course_id"];
#             Question_desc=request.POST.get("Question-"+str(i+1),'')
#             Option1=request.POST.get("Question-"+str(i+1), '')
#             Option1=request.POST.get("Option1-"+str(i+1), '')
#             Option2=request.POST.get("Option2-"+str(i+1), '')
#             Option3=request.POST.get("Option3-"+str(i+1), '')
#             Option4=request.POST.get("Option4-"+str(i+1), '')
#             Marks=request.POST.get("Marks-"+str(i+1), '')
#             NegMarks=request.POST.get("NegMarks-"+str(i+1), '')
#             correct_option=request.POST.get("Correct-"+str(i+1),'')
            
#             print("Question : ",Question)
#             print("Question Quiz: ",Question_quiz)
#             print('Option1: ',Option1)
#             print("Option2: ",Option2)
#             print("Option3 ",Option3)
#             print("Option4 ",Option4)
#             print("Marks ",Marks)
#             print("NegMarks ",NegMarks)
#             print("correct_option ",correct_option)
#             # class Question(models.Model):

#             question =Question(Question_quiz=Question_quiz,Question_desc=Question_desc,marks=Marks,neg_marks=NegMarks,option1=Option1,option2=Option2,option3=Option3,option4=Option4,correct_option=correct_option)
#             question.save()
        
#         # return render(request, "faculty/ManageQuiz.html",dict)
    
#     dict["flag"]=0;
#     AllQuizes=Quiz.objects.all();
#     quizlist=[];
#     for quizz in AllQuizes:
#         quizlist.append(quizz.Quiz_name)
#     dict["quizlist"]=quizlist
    
    
#     return render(request, "faculty/ManageQuiz.html",dict)

def messadmin_logout(request):
    logout(request)
    return HttpResponse("Admin Logout Successfully")
    # return redirect(FacultyLogin)