from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

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