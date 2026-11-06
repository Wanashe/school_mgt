from django import forms
from .models import AcademicYear, Term, GradeLevel, Subject


class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['name', 'start_date', 'end_date', 'is_current']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['name', 'academic_year', 'start_date', 'end_date', 'is_current']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class GradeLevelForm(forms.ModelForm):
    class Meta:
        model = GradeLevel
        fields = ['name', 'description']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'grade_levels', 'description']
        widgets = {
            'grade_levels': forms.CheckboxSelectMultiple,
        }