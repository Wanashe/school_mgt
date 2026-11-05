from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_redirect_view(request):
    user = request.user
    if user.role == 'ADMIN':
        return redirect('admin_dashboard')  # We will map this in dashboard app
    elif user.role == 'TEACHER':
        return redirect('teacher_dashboard')
    elif user.role == 'STUDENT':
        return redirect('student_dashboard')
    elif user.role == 'PARENT':
        return redirect('parent_dashboard')
    elif user.role == 'ACCOUNTANT':
        return redirect('accountant_dashboard')
    else:
        return redirect('admin:index')