from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    context = {}
    return render(request, 'index.html', context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context)


def courses(request):
    context = {}
    return render(request, 'course.html', context)