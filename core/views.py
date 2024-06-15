from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import *
from .forms import CheckoutForm
from paypal.standard.forms import PayPalPaymentsForm

from django.urls import reverse
from django.http import HttpResponse, HttpResponseServerError

import uuid


def index(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'index.html', context)


def about_us(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'about-us.html', context)


def faq(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'faq.html', context)


def blog(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
        "page_obj": page_obj,
        "categories": categories,
        "tags": tags,
    }
    return render(request, 'blog.html', context)


def blog_post(request, id):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'blog-post.html', context)


def courses(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_count = len(request.session.get('cart', []))
    cart_ids = request.session.get('cart', [])

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "tags": tags,
        "cart_count": cart_count,
        "cart_ids": cart_ids,
    }
    return render(request, 'course.html', context)


def add_to_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    cart = request.session.get('cart', [])
    if course.id not in cart:  # Check if the course is not already in the cart
        cart.append(course.id)
        request.session['cart'] = cart
    return redirect('courses')


def remove_from_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    cart = request.session.get('cart', [])
    if course.id in cart:
        cart.remove(course.id)
        request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart_ids = request.session.get('cart', [])
    cart_courses = Course.objects.filter(id__in=cart_ids)
    cart_count = len(request.session.get('cart', []))
    total_price = sum(course.price for course in cart_courses)
    context = {
        'cart_courses': cart_courses,
        'total_price': total_price,
        'cart_count': cart_count,
    }
    return render(request, 'cart.html', context)


def course_detail(request, id):
    context = {}
    return render(request, 'course-detail.html', context)

@csrf_exempt
def checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('home')

    cart_courses = Course.objects.filter(id__in=cart)
    total = sum(course.price for course in cart_courses)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": total,
        "item_name": "Course Purchase",
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('payment-success')),
        "cancel_return": request.build_absolute_uri(reverse('payment-failed')),
    }

    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    checkout_form = CheckoutForm()

    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            checkout = checkout_form.save(commit=False)
            checkout.total = total
            checkout.save()
            checkout.courses.set(cart_courses)
            checkout.save()

            request.session['checkout_id'] = checkout.id  # Store checkout ID in session

            return HttpResponse(paypal_form.render())

    context = {
        'paypal_form': paypal_form,
        'checkout_form': checkout_form,
        'cart_courses': cart_courses,
        'total': total,
        'cart_count': len(cart),
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }
    return render(request, 'checkout.html', context)

@csrf_exempt
def payment_success(request):
    checkout_id = request.session.get('checkout_id')
    if checkout_id:
        try:
            checkout = Checkout.objects.get(id=checkout_id)
            checkout.status = 'COMPLETED'
            checkout.save()
            del request.session['checkout_id']
            request.session['cart'] = []
            return render(request, 'payment_success.html', {'checkout': checkout})
        except Checkout.DoesNotExist:
            return render(request, 'payment_error.html')
    return redirect('home')

@csrf_exempt
def payment_error(request):
    checkout_id = request.session.get('checkout_id')
    if checkout_id:
        try:
            checkout = Checkout.objects.get(id=checkout_id)
            checkout.status = 'FAILED'
            checkout.save()
            del request.session['checkout_id']
            return render(request, 'payment_error.html', {'checkout': checkout})
        except Checkout.DoesNotExist:
            return render(request, 'payment_error.html')
    return redirect('home')

def contact(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'contact.html', context)
