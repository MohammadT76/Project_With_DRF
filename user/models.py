from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.



class User (AbstractUser):
    is_author = models.BooleanField(default = False)
    special_user_time = models.DateTimeField(default = timezone.now)

    def IsSpecialUser (self):
        if self.special_user_time > timezone.now():
            return True
        else:
            return False

    IsSpecialUser.boolean = True
    IsSpecialUser.short_description = 'SpecialUser Status'