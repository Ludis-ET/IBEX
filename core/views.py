from django.core.paginator import Paginator
from django.shortcuts import render

from .models import *




def index(request):
    context = {}
    return render(request, 'index.html', context)



def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
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