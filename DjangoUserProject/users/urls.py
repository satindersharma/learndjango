from django.urls import path, include
from .views import Home, UserLoginView, UserLogoutView, SignUpView


urlpatterns = [
    path('', Home.as_view()),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('', include('django.contrib.auth.urls')),
]
