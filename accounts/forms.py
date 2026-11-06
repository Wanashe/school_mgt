from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from students.models import Student
from teachers.models import Teacher
from academics.models import GradeLevel, Subject


class AdminStudentCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ['admission_number', 'grade_level']

    def save(self, commit=True):
        # Create the base user with role STUDENT
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            role='STUDENT'
        )
        
        # Create the student profile linked to this user
        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student


class AdminTeacherCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ['employee_id', 'qualification', ]
        widgets = {
            'subjects_taught': forms.CheckboxSelectMultiple,
        }

    def save(self, commit=True):
        # Create the base user with role TEACHER
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            role='TEACHER'
        )
        
        # Create the teacher profile linked to this user
        teacher = super().save(commit=False)
        teacher.user = user
        if commit:
            teacher.save()
            self.save_m2m()  # Saves Many-to-Many subjects_taught
        return teacher