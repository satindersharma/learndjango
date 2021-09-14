from django import forms


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=50,required=True)
    age = forms.IntegerField(required=True,max_value=100, min_value=10)
    description = forms.CharField()

