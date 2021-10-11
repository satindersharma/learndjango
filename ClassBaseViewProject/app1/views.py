from django.shortcuts import render

from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Employee
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.


class Home(View):

    def get(self, request):
        return HttpResponse('<h1>Heloo home</h1>')


def html_home(request):
    context = {'name': 'geeta'}
    return render(request, 'home.html', context)


class MyHome(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # to overwrite context
        context = super().get_context_data(**kwargs)
        context['name'] = 'ravan'
        return context


# CURDL


class AllEmployee(ListView):
    template_name = 'emp_list.html'
    # all = Employee.objects.all()
    # it create a context varialbe object_list
    # object_list = Employee.objects.all()
    model = Employee


class EmployeeDetail(DetailView):
    template_name = 'employee_detail.html'
    model = Employee
    # object = Emplyee.objects.get(pk=pk)


class CreateEmployee(CreateView):
    model = Employee
    fields = '__all__'
    # form = EmployeeFrom()
    template_name = 'emp_form.html'
    # reverse_lazy reqire url name
    # success_url is the url to redirect after sccefully created
    success_url = reverse_lazy('all_empoyee')


class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'emp_form.html'
    success_url = reverse_lazy('all_empoyee')


class DeleteEmployee(DeleteView):
    model = Employee
    fields = '__all__'
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('all_empoyee')
