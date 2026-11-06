from django.db import models
from accounts.models import User
from academics.models import GradeLevel

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    admission_number = models.CharField(max_length=50, unique=True)
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.SET_NULL, null=True, related_name='students')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Guardian / Parent Info
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)
    parent_email = models.EmailField(blank=True, null=True)

    admission_date = models.DateField(auto_now_add=True)
    is_graduated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.admission_number})"