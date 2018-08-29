"""Defines URL patterns for users"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
	#Login page
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name= 'login'),
	#login tells django to send req to django's default login view 
	#pass a dictionary telling django where to find the template
	
	#Logout page
	re_path(r'^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
	
	#Registration page
	re_path(r'^register/$', views.register, name = 'register'),
	#this matches URL <http://localhost:8000/users/register/ and sends requests
	#to the register() function 
	]