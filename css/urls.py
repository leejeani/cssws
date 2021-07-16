"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from css import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('register', views.register, name='register'),
    path('registerimpl', views.registerimpl, name='registerimpl'),
    path('html5', views.html5, name='html5'),
    path('css3', views.css3, name='css3'),
    path('javascript', views.javascript, name='javascript'),
    path('jquery', views.jquery, name='jquery'),
    path('ajax', views.ajax, name='ajax'),

    path('userlist', views.userlist, name='userlist'),
    path('userdetail', views.userdetail, name='userdetail'),
    path('additem', views.additem, name='additem'),
    path('additemimpl', views.additemimpl, name='additemimpl'),
    path('itemlist', views.itemlist, name='itemlist'),
    path('itemdetail', views.itemdetail, name='itemdetail'),
]










