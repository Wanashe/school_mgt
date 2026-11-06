from django.urls import path
from . import views

urlpatterns = [
    path('', views.academics_home, name='academics_home'),
    path('year/add/', views.add_academic_year, name='add_academic_year'),
    path('grade/add/', views.add_grade_level, name='add_grade_level'),
    path('subject/add/', views.add_subject, name='add_subject'),
    path('term/add/', views.add_term, name='add_term'),
]