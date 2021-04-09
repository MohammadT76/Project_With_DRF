from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.


UserAdmin.fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser' , 'is_author' , 'special_user_time', 'groups', 'user_permissions')

UserAdmin.list_display += ('IsSpecialUser',)

admin.site.register(User, UserAdmin)
