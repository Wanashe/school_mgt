from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AcademicYear, Term, GradeLevel, Subject
from .forms import AcademicYearForm, TermForm, GradeLevelForm, SubjectForm

# Create your views here.

@login_required
def academics_home(request):
    academic_years = AcademicYear.objects.all()
    grade_levels = GradeLevel.objects.all()
    subjects = Subject.objects.all()
    context = {
        'academic_years': academic_years,
        'grade_levels': grade_levels,
        'subjects': subjects,
    }
    return render(request, 'academics/academics_home.html', context)


@login_required
def add_academic_year(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics_home')
    else:
        form = AcademicYearForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Add Academic Year'})


@login_required
def add_grade_level(request):
    if request.method == 'POST':
        form = GradeLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics_home')
    else:
        form = GradeLevelForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Add Grade Level'})


@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics_home')
    else:
        form = SubjectForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Add Subject'})

@login_required
def add_term(request):
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics_home')
    else:
        form = TermForm()
    return render(request, 'academics/form_template.html', {'form': form, 'title': 'Add Term'})