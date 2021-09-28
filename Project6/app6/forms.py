from django import forms





# class EmployeeForm(forms.Form):
#     idno = forms.IntegerField(label="IDNO")
#     name = forms.CharField(label="NAME")
#     salary = forms.DecimalField(label="SALARY",help_text="Enter Salary in Decimal")
#     items = (
#         ("manager","MANAGER"),
#         ("developer","DEVELOPER"),
#         ("tester","TESTER"),
#     )
#     desig = forms.ChoiceField(label="DESIGNATION",choices=items)
#     doj = forms.DateField(widget=forms.SelectDateWidget,label="DATE OF JOIN")
#     email = forms.EmailField(label="EMAIL")
#     image = forms.FileField(label="PHOTO")
#     password = forms.CharField(label="PASSWORD",widget=forms.PasswordInput)
#     lang1 = forms.BooleanField(label="C-Lang")
#     lang2 = forms.BooleanField(label="C++")
#     lang3 = forms.BooleanField(label="Python")

#     items1 = (
#         ("one","Yes"),
#         ("two","Maybe"),
#         ("three","No"),
#     )
#     status = forms.ChoiceField(label="Are you Attending",choices=items1,widget=forms.RadioSelect)
#     status1 = forms.MultipleChoiceField(label="Are you Attending",choices=items1)
    



class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=50,required=True)
    age = forms.IntegerField(required=True,max_value=100, min_value=10)
    description = forms.CharField(widget=forms.Textarea)


    def clean_age(self):
        # one way
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Only 18+ allowed')
        return age

    def clean_name(self):
        # another way
        name = self.cleaned_data['name']
        if (name == 'geeta') or (name == 'Geeta'):
            self.add_error('name','Geeta is not allowd')
        return name


POSTION_CHOICES =(
    ('mng','Manager'),
    ('dev','Devloper'),
    ('tst','Tester')
)

ITEMS1 = (
        ("one","Yes"),
        ("two","Maybe"),
        ("three","No"),
    )
class SoftwareEmployeeForm(forms.Form):
    idno = forms.IntegerField()
    name = forms.CharField()
    salary = forms.DecimalField()
    position = forms.ChoiceField(choices=POSTION_CHOICES)
    date_of_join = forms.DateField(widget=forms.SelectDateWidget)
    email = forms.EmailField()
    file_f = forms.FileField(label="FIle")
    password = forms.CharField(widget=forms.PasswordInput)
    lang1 = forms.BooleanField(label="C-Lang")
    lang2 = forms.BooleanField(label="C++")
    lang3 = forms.BooleanField(label="Python")
    marriage_status = forms.ChoiceField(choices=ITEMS1,widget=forms.RadioSelect)



