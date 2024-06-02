from django.urls import path
from . import views

urlpatterns = [
    path("checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("myfcourses",views.facultycourses,name="facultycourses"),
    path("facultychangepwd",views.facultychangepwd,name="facultychangepwd"),
    path("facultyupdatedpwd",views.facultyupdatedpwd,name="facultyupdatedpwd"),
    path("uploadcoursecontent",views.uploadcoursecontent,name="uploadcoursecontent"),
 ]