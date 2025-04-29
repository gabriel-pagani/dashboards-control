from django.contrib import admin
from django.urls import path
from app.views import home, users, dashboards


urlpatterns = [
    path('', home),
    path('users', users),
    path('dashboards', dashboards),
]
