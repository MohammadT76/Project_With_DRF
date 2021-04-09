from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics

# Create your views here.


class blog_api (generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_publish = True)
    serializer_class = BlogSerializer