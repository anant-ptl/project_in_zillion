"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from library import views

urlpatterns = [
    path('', views.register_page, name='registration'),
    path('login_page/', views.login_page, name='login_page') ,
    path('normal_user/', views.normal_user, name='normal_user'),
    path('librarian_page/', views.librarian_page, name='librarian'),
    path('stock_status/', views.stock_status, name='stock_status'),
    path('available_books/', views.available_books, name='available_books'),
    path('approved_request/', views.approved_request, name='approved_request'),    
    path('assigned_books/', views.assigned_books, name='assigned_books'),
    path('assign_books/', views.assign_books, name='assign_books'),
    path('logout/', views.logout_view, name='logout')
]
