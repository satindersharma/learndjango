"""Project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app5.views import home,showemployee, deleteemployee, employee_form, update_employee
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('emp/<int:pk>/',showemployee),
    path('emp/<int:pk>/delete/',deleteemployee),
    path('create/',employee_form),
    path('update/<int:pk>/',update_employee),
]
