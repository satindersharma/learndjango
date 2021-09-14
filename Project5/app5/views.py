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



def employee_form(request):




    print("Currunt request METHOD ",request.method)
    print("value on request POST ",request.POST)
    # print("value on request GET ",request.GET)
    #Currunt request METHOD  POST
    # value on request POST  
    # <QueryDict: {'csrfmiddlewaretoken': ['WVzbKEys58vndChyPuqPy6Mh8fDHgST3Gz8wJ9xcSH51DU5TmPecJZMnquqFF43L'], 'name': ['geet'], 'age': ['34'], 'discription': ['fgsdhgfgs']}>
    context = {}
    if request.method == 'POST':
        
        name = request.POST['name']
        age = request.POST['age']
        desc = request.POST['discription']
        if not isinstance(age,int):
            context = {'msg':'please enter number for age'}
            return render(request,'employee_form.html',context)
        # print(name, age, desc)
        context = {'msg':'new employee saved successfully'}
        Employee.objects.create(name=name,age=age,description=desc)



    return render(request,'employee_form.html',context)




def update_employee(request,pk):
    single_emp = Employee.objects.get(pk=pk)

    # single_emp.update()
    # emp = Employee.objects.filter(age=32)
    # emp = Employee.objects.all()
    # print(emp)
    context={'single_emp':single_emp}
    if request.method == 'POST':
        
        name = request.POST['name']
        age = request.POST['age']
        desc = request.POST['discription']
        # print(name, age, desc)
        context = {'msg':' employee updated successfully',
                    'single_emp':single_emp}
        single_emp.name = name
        single_emp.age = age
        single_emp.description = desc
        single_emp.save()
        # single_emp.update(name=name,age=age,description=desc)
    return render(request,'employee_form_update.html',context)