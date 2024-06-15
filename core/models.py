import pycountry
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    poster = models.ImageField(upload_to='blog-posts-poster/', null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    poster = models.ImageField(upload_to='course-posters/')
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name='courses')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    interval = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Checkout(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(
        max_length=255,
        choices=[(country.name, country.name) for country in pycountry.countries],
        default='United States'
    )
    courses = models.ManyToManyField(Course)
    total = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.total}'