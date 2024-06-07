from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    poster = models.ImageField(upload_to='blog-posts-poster/', null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
