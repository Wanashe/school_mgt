from django.db import models

# Create your models here.

class AcademicYear(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "2026/2027"
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Term 1", "Term 2"
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='terms')
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.academic_year.name} - {self.name}"


class GradeLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "Form 1", "Grade 8"
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Mathematics", "Physics"
    code = models.CharField(max_length=20, unique=True)  # e.g., "MATH101"
    grade_levels = models.ManyToManyField(GradeLevel, related_name='subjects')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"