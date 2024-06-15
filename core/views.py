from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError
from django.core.paginator import Paginator
from .models import *
from .forms import CheckoutForm
import paypalrestsdk

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox or live
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})

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

def checkout(request):
    cart_ids = request.session.get('cart', [])
    if not cart_ids:
        return redirect('index')

    cart_courses = Course.objects.filter(id__in=cart_ids)
    total_price = sum(course.price for course in cart_courses)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.total = total_price
            checkout.save()
            for course in cart_courses:
                checkout.courses.add(course)

            # Create PayPal payment
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": request.build_absolute_uri('/execute_payment/'),
                    "cancel_url": request.build_absolute_uri('/payment_cancel/')
                },
                "transactions": [{
                    "item_list": {
                        "items": [{
                            "name": "Course Purchase",
                            "sku": "course",
                            "price": str(total_price),
                            "currency": "USD",
                            "quantity": 1
                        }]
                    },
                    "amount": {
                        "total": str(total_price),
                        "currency": "USD"
                    },
                    "description": "Purchase of online courses"
                }]
            })

            if payment.create():
                for link in payment.links:
                    if link.rel == "approval_url":
                        approval_url = str(link.href)
                        return redirect(approval_url)
            else:
                return HttpResponseServerError("Failed to create PayPal payment.")

    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form, 'cart_courses': cart_courses, 'total_price': total_price})

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    if not payment_id or not payer_id:
        return HttpResponseServerError("Payment ID or Payer ID not provided.")

    try:
        payment = paypalrestsdk.Payment.find(payment_id)
    except paypalrestsdk.exceptions.PayPalRESTException as e:
        return HttpResponseServerError(f"Failed to retrieve payment details: {e}")

    if not payment:
        return HttpResponseServerError("Payment not found.")

    try:
        if payment.execute({"payer_id": payer_id}):
            transaction = payment.transactions[0]
            related_resources = transaction.related_resources[0]
            sale = related_resources.sale
            checkout = get_object_or_404(Checkout, paypal_transaction_id=payment_id)
            checkout.status = 'COMPLETED'
            checkout.save()
            return render(request, 'checkout_success.html', {'checkout': checkout})
        else:
            return render(request, 'checkout_failed.html')
    except paypalrestsdk.exceptions.PayPalRESTException as e:
        return HttpResponseServerError(f"Failed to execute payment: {e}")

def contact(request):
    cart_count = len(request.session.get('cart', []))
    context = {
        "cart_count": cart_count,
    }
    return render(request, 'contact.html', context)
