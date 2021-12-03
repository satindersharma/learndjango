from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Course, FeedBack


class Home(TemplateView):
    template_name = 'home.html'



class AboutUs(TemplateView):
    template_name = 'about-us.html'



class CourseListView(ListView):
    model = Course
    template_name="course_list.html"


class Feedback(TemplateView):
    template_name = "feedback.html"