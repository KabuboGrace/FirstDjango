from django import forms
from Myapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields= []