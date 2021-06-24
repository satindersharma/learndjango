from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def geetahello(request):
    return HttpResponse("<h1>Hello from geeta</h1>")


def geetanew(request):
    now = datetime.now()
    context = {"nam":"Satinder",
                "abhi":now}
    return render(request,'geeta.html',context=context)