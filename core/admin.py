from django.contrib import admin
from .models import Category, Tag, Blog, Course, Checkout

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'posted_date']
    list_filter = ['author', 'tags']
    search_fields = ['title', 'description']

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'poster', 'description')
        }),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('tags')
        }),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'date']
    list_filter = ['category']
    search_fields = ['title', 'description']

    fieldsets = (
        (None, {
            'fields': ('title', 'poster', 'description', 'price', 'interval')
        }),
        ('Categories', {
            'classes': ('collapse',),
            'fields': ('category',)
        }),
    )

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status', 'date']
    list_filter = ['status']
    search_fields = ['first_name', 'last_name', 'email', 'address', 'city', 'state', 'postal_code', 'country']

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'address', 'city', 'state', 'postal_code', 'country')
        }),
        ('Courses Purchased', {
            'classes': ('collapse',),
            'fields': ('courses', 'total')
        }),
        ('Payment Information', {
            'classes': ('collapse',),
            'fields': ('status', 'paypal_transaction_id')
        }),
    )
