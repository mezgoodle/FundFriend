from django.contrib import admin

from core.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
