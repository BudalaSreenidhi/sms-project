from django import forms

from adminapp.models import Faculty,Student


class AddFacultyForm(forms.ModelForm):
     class Meta:
          model = Faculty
          fields = "__all__"
          exclude = {"password"}
          labels = {"faculty_id":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Fullname"}

class AddStudentForm(forms.ModelForm):
     class Meta:
          model = Student
          fields = "__all__"
          exclude = {"password"}
          labels = {"student_id":"Enter Student ID","gender":"Select Gender"}

class StudentForm(forms.ModelForm):
     class Meta:
          model = Student
          fields = "__all__"
          exclude = {"student_id"}

class FacultyForm(forms.ModelForm):
     class Meta:
          model = Faculty
          fields = "__all__"
          exclude = {"faculty_id"}