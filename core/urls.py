from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),

    path('about-us/', about_us, name="about"),
    
    path('faq/', faq, name="faq"),

    path('blogs/', blog, name="blog"),
    path('blog-post/<id>/', blog_post, name="blog-post"),

    path('courses/', courses, name='courses'),

    path('add-to-cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:course_id>/', remove_from_cart, name='remove_from_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),

    path('contact-us/', contact, name="contact"),

    path('paypal/<int:checkout_id>/', paypal_checkout, name='paypal_checkout'),
]
