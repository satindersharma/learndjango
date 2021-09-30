from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    #499
    geeta = forms.CharField()
    class Meta:
        model = Employee
        # fields = ('name','age','position')
        fields = '__all__'
        exclude = ('position','age')



# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'
