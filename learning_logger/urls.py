"""learning_logger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
	re_path(r'^users/', include('users.urls')), 
	#distinguish URLs that belong to learning_logs app vs users app
	re_path(r'', include('learning_logs.urls')),
	#the URLS defined in learning_logs.urls will have an app namespace learning_logs:
	#ths is defined in the respective apps' url.py
]
