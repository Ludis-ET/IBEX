from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import *
from .forms import CheckoutForm




def index(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count":cart_count,
    }
    return render(request, 'index.html', context)


def about_us(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count":cart_count,
    }
    return render(request, 'about-us.html', context)


def faq(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count":cart_count,
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
        "cart_count":cart_count,
        "page_obj": page_obj,
        "categories":categories,
        "tags":tags,
    }
    return render(request, 'blog.html', context)


def blog_post(request, id):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count":cart_count,
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
        "cart_count":cart_count,
        "cart_ids":cart_ids,
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


def checkout(request):
    cart_count = len(request.session.get('cart', []))
    cart_ids = request.session.get('cart', [])
    if not cart_ids:
        return redirect('home')

    cart_courses = Course.objects.filter(id__in=cart_ids)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            total = sum(course.price for course in cart_courses)
            checkout = Checkout(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                postal_code=form.cleaned_data['postal_code'],
                country=form.cleaned_data['country'],
                total=total
            )
            checkout.save()
            checkout.courses.set(cart_courses)
            # Simulate payment process
            payment_successful = process_payment(checkout.total)
            if payment_successful:
                checkout.status = 'COMPLETED'
            else:
                checkout.status = 'FAILED'
            checkout.save()
            # Clear the cart
            request.session['cart'] = []
            return render(request, 'checkout_success.html', {'checkout': checkout})
    else:
        form = CheckoutForm()

    # Calculate the total
    total = sum(course.price for course in cart_courses)

    return render(request, 'checkout.html', {'form': form, 'cart_courses': cart_courses, 'total': total, 'cart_count':cart_count})

def process_payment(total):
    # Simulate payment processing
    # Replace with actual payment processing logic
    return True  # Assume payment is always successful for this example



def contact(request):
    
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count":cart_count,
    }
    return render(request, 'contact.html', context)