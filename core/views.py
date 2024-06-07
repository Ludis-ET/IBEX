from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    context = {}
    return render(request, 'index.html', context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context)


def blog_post(request, id):
    context = {}
    return render(request, 'blog-post.html', context)


def courses(request):
    context = {}
    return render(request, 'course.html', context)


def course_detail(request, id):
    context = {}
    return render(request, 'course-detail.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)