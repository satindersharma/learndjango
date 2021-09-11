from django.shortcuts import render
from .models import Employee
# Create your views here.
def home(request):
    # emp = Employee.objects.filter(age=32)
    emp = Employee.objects.reverse()
    print(emp)
    context={'emp':emp}
    return render(request,'home.html',context)



def showemployee(request,pk):
    single_emp = Employee.objects.get(pk=pk)
    # print(single_emp)

    context = {'single_emp':single_emp}
    # context = {}
    return render(request,'employee.html',context)



def deleteemployee(request,pk):
    single_emp = Employee.objects.get(pk=pk)
    single_emp.delete()
    # emp = Employee.objects.filter(age=32)
    emp = Employee.objects.all()
    # print(emp)
    context={'emp':emp}
    return render(request,'home.html',context)