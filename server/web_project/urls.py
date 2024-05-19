"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from server_with_model import views

urlpatterns = [
    path('take_code', views.take_code),  # post
    path('find_code', views.find_code),  # post
    path('send_init_ecg', views.send_init_ecg),  # post
    path('check_ecg', views.check_ecg),  # post
    path('close_check_ecg', views.close_check_ecg),  # post
    path('close_desktop', views.close_desktop),  # post
]
