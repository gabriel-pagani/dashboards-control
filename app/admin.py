from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Dashboard


class DashboardInline(admin.TabularInline):  # ou StackedInline se preferir
    model = Dashboard
    extra = 1  # quantos campos vazios aparecem por padrão

# Extende o UserAdmin para incluir os Dashboards


class UserAdmin(BaseUserAdmin):
    inlines = [DashboardInline]


# Remove o registro original e registra o novo
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
