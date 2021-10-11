from django.urls import path
from .views import Home, html_home, MyHome, AllEmployee,EmployeeDetail,  CreateEmployee, UpdateEmployee, DeleteEmployee

'''
pehla type
dusra database table ka field
<int:pk>

'''

urlpatterns = [
    path('',Home.as_view(),name='redrer'),
    path('home/',html_home),
    path('home2/',MyHome.as_view()),
    path('all/',AllEmployee.as_view(), name='all_empoyee'),
    path('create/',CreateEmployee.as_view(),name='create-emp'),
    path('detail/<int:pk>/',EmployeeDetail.as_view(),name='detail-emp'),
    path('update/<int:pk>/',UpdateEmployee.as_view(),name='update-emp'),
    path('delete/<int:pk>/',DeleteEmployee.as_view(),name='delete-emp'),

]