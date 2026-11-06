from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student
from teachers.models import Teacher
from academics.models import AcademicYear, Term, GradeLevel, Subject

# Create your views here.

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def admin_dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'current_year': AcademicYear.objects.filter(is_current=True).first(),
        # 'total_academic_years': AcademicYear.objects.count(),
        # 'total_terms': Term.objects.count(),
        # 'total_grade_levels': GradeLevel.objects.count(),
        # 'total_subjects': Subject.objects.count(),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')

@login_required
def parent_dashboard(request):
    return render(request, 'dashboard/parent_dashboard.html')

@login_required
def accountant_dashboard(request):
    return render(request, 'dashboard/accountant_dashboard.html')