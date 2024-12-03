from django.contrib import admin
from django.urls import path, include
from .views import login_view, home_view,logout_view,signup_view,teacher_home,student_home,principal_home

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('teacher_home/', teacher_home, name='teacher_home'),
    path('student_home/', student_home, name='student_home'),
    path('principal_home/', principal_home, name='principal_home'),    
]