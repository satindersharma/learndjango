from django.shortcuts import render
from .models import Employee
# Create your views here.

print(__name__)
def home(request):

    employe = Employee.objects.all()
    context = {"namwa":"geeta",
                "age":36,
                "athlete_list":["geeta","renu","swati","satti"],
                "is_zinda":False,
                "emp":employe

    }
    return render(request,'home.html',context)