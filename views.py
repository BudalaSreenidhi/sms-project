from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from adminapp.models import Admin, Student, Faculty, Course, FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm, StudentForm, FacultyForm


def adminhome(request):
    auname = request.session["auname"]
    return render(request, "adminhome.html", {"adminuname": auname})


def logout(request):
    return render(request, "login.html")


def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]
    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        print("login sucess")
        request.session["auname"] = adminuname
        return render(request, "adminhome.html", {"adminuname": adminuname})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"message": msg})
        # return HttpResponse("Login Failed")


def viewstudents(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "viewstudents.html", {"studentdata": students, "count": count, "adminuname": auname})


def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "viewfaculty.html", {"facultydata": faculty, "count": count, "adminuname": auname})


def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "viewcourses.html", {"coursesdata": courses, "count": count, "adminuname": auname})


def adminstudent(request):
    auname = request.session["auname"]
    return render(request, "adminstudent.html", {"adminuname": auname})


def adminfaculty(request):
    auname = request.session["auname"]
    return render(request, "adminfaculty.html", {"adminuname": auname})


def admincourse(request):
    auname = request.session["auname"]
    return render(request, "admincourse.html", {"adminuname": auname})


def addcourse(request):
    auname = request.session["auname"]
    return render(request, "addcourse.html")


def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "updatecourse.html", {"adminuname": auname, "courses": courses, "count": count})


def courseupdation(request, cid):
    auname = request.session["auname"]
    return render(request, "courseupdation.html", {"cid": cid, "adminuname": auname})


def courseupdated(request):
    auname = request.session["auname"]

    cid = request.POST["cid"]
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]

    Course.objects.filter(id=cid).update(course_title=ctitle, ltps=ltps, credits=credits)
    msg = "Course Updated Successfully"

    return render(request, "courseupdation.html", {"msg": msg, "adminuname": auname})


def insertcourse(request):
    auname = request.session["auname"]
    if request.method == "POST":
        dept = request.POST["dept"]
        program = request.POST["program"]
        ay = request.POST["ay"]
        sem = request.POST["sem"]
        year = request.POST["year"]
        ccode = request.POST["ccode"]
        ctitle = request.POST["ctitle"]
        ltps = request.POST["ltps"]
        credits = request.POST["credits"]
        course = Course(department=dept, program=program, academic_year=ay, semester=sem, year=year, course_code=ccode,
                        course_title=ctitle, ltps=ltps, credits=credits)

        Course.save(course)
        message = "Course Added Successfully"
        return render(request, "addcourse.html", {"msg": message, "adminuname": auname})


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count, "adminuname": auname})


def coursedeletion(request, cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")


def addfaculty(request):
    auname = request.session["auname"]
    form = AddFacultyForm()
    if request.method == "POST":
        form1 = AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            # return HttpResponse("Faculty Added Successfully")
            message = "Faculty Added Successfully"
            return render(request, "addfaculty.html", {"msg": message, "form": form, "adminuname": auname})
        else:
            message = "Failed to Add Faculty"
            return render(request, "addfaculty.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request, "addfaculty.html", {"form": form, "adminuname": auname})


def updatefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatefaculty.html", {"facultydata": faculty, "count": count, "adminuname": auname})


def facultyupdation(request, fid):
    auname = request.session["auname"]
    faculty = get_object_or_404(Faculty, pk=fid)
    if request.method == "POST":
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Updated Successfully")
        else:
            return HttpResponse("Updation Failed")
    else:
        form = FacultyForm(instance=faculty)
    return render(request, "facultyupdated.html", {"form": form, "adminuname": auname})


def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count, "adminuname": auname})


def facultydeletion(request, fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")


def addstudent(request):
    auname = request.session["auname"]
    form = AddStudentForm()
    if request.method == "POST":
        form1 = AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            # return HttpResponse("Faculty Added Successfully")
            message = "Student Added Successfully"
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})
        else:
            message = "Failed to Add Student "
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request, "addstudent.html", {"form": form, "adminuname": auname})


def updatestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "updatestudent.html", {"studentsdata": student, "count": count, "adminuname": auname})


def studentupdation(request, sid):
    auname = request.session["auname"]
    student = get_object_or_404(Student, pk=sid)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Updated Successfully")
        else:
            return HttpResponse("Updation Failed")
    else:
        form = StudentForm(instance=student)
    return render(request, "studentupdated.html", {"form": form, "adminuname": auname})


def deletestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentsdata": student, "count": count, "adminuname": auname})


def studentdeletion(request, sid):
    Student.objects.filter(sid=sid).delete()
    return redirect("deletestudent")


def facultycoursemapping(request):
    fmcourses = FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    count = FacultyCourseMapping.objects.count()
    return render(request, "facultycoursemapping.html", {"adminuname": auname, "fmcourses": fmcourses, "count": count})


def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request, "adminchangepwd.html", {"adminuname": auname})


def adminupdatedpwd(request):
    auname = request.session["auname"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    flag = Admin.objects.filter(Q(username=auname) & Q(password=opwd))
    if flag:
        print("Old pwd is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated")
        msg = "Password Updated Successfully"
    else:
        print("Old pwd is Invalid")
        msg = "Old Password is Incorrect"
    return render(request, "adminchangepwd.html", {"adminuname": auname, "message": msg})
