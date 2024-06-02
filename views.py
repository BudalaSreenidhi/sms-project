from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from adminapp.models import Student,Course
from facultyapp.models import CourseContent

def studenthome(request):
    sid = request.session["sid"]
    student=Student.objects.get(student_id=sid)
    print(student)
    return render(request,"studenthome.html",{"sid":sid,"student":student})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag = Student.objects.filter(Q(student_id=sid) & Q(password=pwd))  # Update 'studentid' to 'student_id'
    print(flag)

    if flag:
        print("login sucess")
        request.session["sid"] = sid
        student = Student.objects.get(student_id=sid)
        return render(request, "studenthome.html", {"sid": sid,"student":student})
    else:
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message": msg})

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})

def studentupdatedpwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    flag=Student.objects.filter(Q(student_id=sid)& Q(password=opwd))
    if flag:
        print("Old pwd is Correct")
        Student.objects.filter(student_id=sid).update(password=npwd)
        print("updated")
        msg = "Password Updated Successfully"
    else:
        print("Old pwd is Invalid")
        msg = "Old Password is Incorrect"
    return render(request,"studentchangepwd.html",{"sid": sid,"message":msg})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid = request.session["sid"]
    content = CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})

def displaystudentcourses(request):
    sid = request.session["sid"]
    ay=request.POST['ay']
    sem = request.POST['sem']

    courses=Course.objects.filter(Q(academic_year=ay)&Q(semester=sem))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})

