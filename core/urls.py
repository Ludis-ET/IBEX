from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('blogs/', blog, name="blog"),
    path('courses/', courses, name="course"),
]
