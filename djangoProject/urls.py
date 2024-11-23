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

from CollectionList import CollectionList
from admin import batchAddToBlacklist
from admin.batchAddToBlacklist import batch_add_blacklist, batch_Remove_Blacklist
from admin.batchDeleteBooks import batchDeleteBook, batchDeleteBooks
from admin.bookListServlet import bookList
from admin.change_user import change_user
from admin.delete_user import delete_user
from admin.editBooks import editBooks, addBooks
from admin.editUser import editUser
from admin.login import admin, loginAdmin
from admin.main import adminMain
from admin.saveUser import saveUser
from admin.toEditBooks import toEditBooks
from admin.updateBook import updateBook
from admin.userListServlet import userList
from back_Book import return_Books
from bookList import Book_List
from borrowBooks.returnBooks import returnBooks
from borrowServlet import borrow_Book
from changePassword import change_password
from collectionServlet import collection_Book
from function4.unconllection import unconllection_t
from searchServlet import search_books
from registServlet import regist
from loginOutServlet import loginOut
from loginServlet import login
from index import *
from unCollection import unCollection

urlpatterns = [
    path('login/', login, name='login'),  # 登录页面
    path('', index, name='index'),  # 主页
    path('register/', regist, name='register'),  # 主页
    path('loginOut/', loginOut, name='loginOut'),  # 登录页面
    path('search_books/', search_books, name='search_books'),
    path('borrow/<int:book_id>/', borrow_Book, name='borrow_Book'),
    path('collection/<int:book_id>/', collection_Book, name='collection_Book'),
    path('Book_List/', Book_List, name='book_list'),
    path('Collection_List/', CollectionList, name='Collection_List'),
    path('back_Book/<str:book_name>/', return_Books, name='back_Book'),
    path('unCollection/<int:book_id>/', unCollection, name='unCollection'),
    path('test/', test, name='test'),
    path('change_password/',change_password,name='change_password'),
    path('loginAdmin/', loginAdmin , name='loginAdmin'),
    path('Admin/', admin, name='Admin'),
    path('AdminMain/', adminMain, name='AdminMain'),
    path('Admin/userList/', userList, name='userList'),
    path('Admin/bookList/', bookList, name='bookList'),
    path('editUser/', editUser, name='editUser'),
    path('change_user/', change_user, name='change_user'),
    path('saveUser/', saveUser, name='saveUser'),

    path('deleteUser/<int:user_id>/', delete_user, name='delete_user'),

    path('batchAddToBlacklist/', batch_add_blacklist, name='batchAddToBlacklist'),

    path('batchRemoveFromBlacklist/', batch_Remove_Blacklist, name='batchRemoveFromBlacklist'),


    path('toEditBooks/', toEditBooks, name='toEditBooks'),
    path('editBooks/', editBooks, name='editBooks'),
    
    path('updateBook/', updateBook, name='updateBook'),
    path('addBooks/', addBooks, name='addBooks'),

    path('batchDeleteBook/<int:book_id>/', batchDeleteBook, name='batchDeleteBook'),
    path('batchDeleteBooks/', batchDeleteBooks, name='batchDeleteBooks'),


]
