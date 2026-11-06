from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.admin_user_management, name='user_management'),
    path('users/register-student/', views.register_student, name='register_student'),
    path('users/register-teacher/', views.register_teacher, name='register_teacher'),
]