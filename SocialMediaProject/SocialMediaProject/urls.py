"""
URL configuration for SocialMediaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# SocialMediaProject/urls.py
from django.contrib import admin
from django.urls import path, include
from socialapp.views import accounts_profile_redirect
from django.contrib.auth import views as auth_views  # <-- Add this import
from socialapp.views import MyLogoutView  # if you're using the custom logout view, otherwise omit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('socialapp.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='socialapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', accounts_profile_redirect, name='accounts_profile_redirect'),

    # Or if using the custom logout view:
    # path('logout/', MyLogoutView.as_view(next_page='login'), name='logout'),
]
