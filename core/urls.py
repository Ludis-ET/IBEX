from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('blogs/', blog, name="blog"),
    path('blog-post/<id>/', blogpost, name="blog-post"),
    path('courses/', courses, name="course"),
    path('contact-us/', contact, name="contact"),
]
