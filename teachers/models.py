from django.db import models
from accounts.models import User
from academics.models import Subject

# Create your models here.

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=100, blank=True, null=True)  # e.g., "B.Ed Mathematics"
    subjects = models.ManyToManyField(Subject, related_name='teachers', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Mr/Ms. {self.user.get_full_name()} ({self.employee_id})"