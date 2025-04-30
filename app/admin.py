from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Dashboard


class DashboardInline(admin.TabularInline):
    model = Dashboard
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = [DashboardInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
