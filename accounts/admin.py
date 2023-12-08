from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'user_role_display'
    )

    def user_role_display(self, obj):
        return obj.get_user_role_display()

    user_role_display.short_description = 'User Role'

admin.site.register(User, UserAdmin)
