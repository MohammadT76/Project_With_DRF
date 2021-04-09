from django.contrib import admin
from django.urls import path , include
from .views import blog_api



app_name = 'blog'


urlpatterns = [
    path('api/' , blog_api.as_view() ),
]