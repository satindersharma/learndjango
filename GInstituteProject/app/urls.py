from django.urls import path
from .views import Home, AboutUs, CourseListView, Feedback


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', AboutUs.as_view(), name="about-us"),
    path('course/', CourseListView.as_view(), name="course"),
    path('feedback/', Feedback.as_view(), name="feedback"),
]
