from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "image", "text" , "category")
    
@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "blog", "comment", "created_at")