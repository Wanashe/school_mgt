from django.contrib import admin
from .models import AcademicYear, Term, GradeLevel, Subject

# Register your models here.

admin.site.register(AcademicYear)
admin.site.register(Term)
admin.site.register(GradeLevel)
admin.site.register(Subject)