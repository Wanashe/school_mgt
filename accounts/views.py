from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdminStudentCreateForm, AdminTeacherCreateForm
from students.models import Student
from teachers.models import Teacher

# Create your views here.

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

@login_required
def admin_user_management(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'students': students,
        'teachers': teachers
    }
    return render(request, 'accounts/user_management.html', context)

@login_required
def register_student(request):
    if request.method == 'POST':
        form = AdminStudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = AdminStudentCreateForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Register New Student'})

@login_required
def register_teacher(request):
    if request.method == 'POST':
        form = AdminTeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = AdminTeacherCreateForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Register New Teacher'})

@login_required
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_to_delete.delete()
        return redirect('user_management')
    return render(request, 'accounts/confirm_delete.html', {'target_user': user_to_delete})