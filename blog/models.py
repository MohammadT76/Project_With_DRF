from django.db import models
from django.contrib.auth.models import AbstractUser
from user.models import User

# Create your models here.




class Blog (models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    desc = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default = False)


    def __str__ (self):
        return self.title