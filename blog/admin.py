from django.contrib import admin
from .models import Blog

# Register your models here.



class admin_blog (admin.ModelAdmin):
    list_display = ('id' , 'author' , 'title' , 'desc' , 'is_publish')

admin.site.register(Blog,admin_blog)