from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from adminapp.models import Faculty,FacultyCourseMapping
from django.shortcuts import render, redirect
from .forms import AddCourseContentForm
from .models import CourseContent


def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]
    flag = Faculty.objects.filter(Q(faculty_id=fid) & Q(password=pwd))  # Update 'studentid' to 'student_id'
    print(flag)

    if flag:
        print("login sucess")
        request.session["fid"] = fid
        return render(request, "facultyhome.html", {"fid": fid})
    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message": msg})

def facultycourses(request):
    fid = request.session["fid"]
    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses = []
    for course in mappingcourses:
        #print(course.faculty.faculty_id)
        if(course.faculty.faculty_id == int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatedpwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    flag=Faculty.objects.filter(Q(faculty_id=fid)& Q(password=opwd))
    if flag:
        print("Old pwd is Correct")
        Faculty.objects.filter(faculty_id=fid).update(password=npwd)
        print("updated")
        msg = "Password Updated Successfully"
    else:
        print("Old pwd is Invalid")
        msg = "Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid": fid,"message":msg})

def uploadcoursecontent(request):
    fid = request.session["fid"]
    if request.method == 'POST':
        form = AddCourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract data from the form
            faculty_id = request.session["fid"]
            faculty = Faculty.objects.get(faculty_id=faculty_id)
            course_id = form.cleaned_data['course'].id
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']
            contentimage = form.cleaned_data['contentimage']

            # Save course content to the database
            course_content = CourseContent.objects.create(
                faculty=faculty,
                course_id=course_id,
                description=description,
                link=link,
                contentimage=contentimage
            )

            # Optionally, you can redirect to a success page
            return redirect('facultyhome')
    else:
        form =AddCourseContentForm()

    # If the request method is GET or form is invalid, render the form again
    return render(request, 'uploadcoursecontent.html', {'form': form,"fid": fid})

