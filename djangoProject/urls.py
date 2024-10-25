"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from IPython.testing.plugin.pytest_ipdoctest import import_path
from django.contrib import admin
from django.urls import path

from searchServlet import search_books
from registServlet import regist
from loginOutServlet import loginOut
from loginServlet import login
from view import *
urlpatterns = [
    path('login/', login, name='login'),  # 登录页面
    path('', index, name='index'),  # 主页
    path('register/', regist, name='register'),  # 主页
    path('loginOut/', loginOut, name='loginOut'),  # 登录页面
    path('search_books/', search_books, name='search_books'),
]
