from authentication import views as user_views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from authentication import views as user_views

urlpatterns = [
    # Homepage URL
    path('', user_views.homepage, name='homepage'),

    # User signup URL
    path('signup', user_views.signup, name='signup'),

    # User login URL
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # User logout URL
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
