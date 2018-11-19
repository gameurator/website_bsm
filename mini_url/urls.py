"""test_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.view_urls, name='url_list'),
    # path('url-formulaire/', views.form_mini_url, name='form_url'),
    url(r'^(?P<code>\w{6})/$', views.redirect_url, name='redirect_url'),
    url(r'^nouveau/$', views.URLCreate.as_view(), name='url_new'),
    url(r'^edition/(?P<code>\w{6})$', views.URLUpdate.as_view(), name='url_update'),
]
