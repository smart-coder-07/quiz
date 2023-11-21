from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [ 
	path('quiz/', views.quiz, name='quiz'), 
	path('api/get-quiz/', views.get_quiz, name='get_quiz'),
	path('',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
] 
