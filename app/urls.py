from django.urls import path
from app.views import login_view, home_view, logout_view, change_password_view


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-change/', change_password_view, name='password-change'),
]
