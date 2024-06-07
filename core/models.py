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
    
