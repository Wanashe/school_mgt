from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('admin-dash/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dash/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dash/', views.student_dashboard, name='student_dashboard'),
    path('parent-dash/', views.parent_dashboard, name='parent_dashboard'),
    path('accountant-dash/', views.accountant_dashboard, name='accountant_dashboard'),
]