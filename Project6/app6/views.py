from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.


def home(request):
    return render(request, 'home.html')


def create_view(request):
    form = EmployeeForm()

    if request.method == 'POST':
        data = request.POST
        form = EmployeeForm(data)
        print(form)
        # print('before form.is_valid()',dir(form))
        # print(form.cleaned_data)
        # print(form.errors)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            description = form.cleaned_data['description']
            # print('after form.is_valid()',dir(form))
            print('form is well and good')
            Employee.objects.create(name=name,
                                    age=age,
                                    description=description)
            # take the blank form
            form = EmployeeForm()
            context = {'msg': 'new employee saved successfully',
                       'form': form
                       }

            return render(request, 'create_form.html', context)

    # when get or error in post
    context = {'form': form}
    return render(request, 'create_form.html', context)
