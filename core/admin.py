from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_date', 'author']
    list_filter = ['author', 'posted_date']
    search_fields = ['title', 'description']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','price','interval']
    list_filter = ['category', 'date']
    search_fields = ['title', 'description']

admin.site.register(Category)
admin.site.register(Checkout)
admin.site.register(Tag)