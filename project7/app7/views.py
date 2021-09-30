from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def home(request):
    form = {'form':EmployeeForm()}
    return render(request, 'create_form.html',context=form)


def emp_list(request):
    object_list = Employee.objects.all()
    context = {
        'object_list':object_list
        }
    return render(request, 'emp_list.html',context=context)