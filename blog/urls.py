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
from . import views
from .models import Article, Categorie
from django.conf.urls import url
from django.views.generic import TemplateView, ListView

urlpatterns = [
    path('contact/', views.contact, name='form_contact'),
    path('blog-formulaire/', views.form_article, name='form_blog'),
    path('accueil/', views.home),
    path('article/<int:id_article>-<slug:slug>', views.view_article, name='afficher_article'),
    path('articles/<int:year>/<int:month>', views.list_articles, name='afficher_liste_dates'),
    path('date', views.date_actuelle, name='date'),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition, name='add'),
    path('faq', views.faq, name='faq'),
    url(r'^faq$', TemplateView.as_view(template_name='blog/faq.html')),
    # Nous demandons la vue correspondant à la classe FAQView
    url(r'^$', views.ListArticles.as_view(), name='home'),
    url(r'categorie/(?P<id>\d+)', views.ListArticles.as_view(), name='blog_categorie'),
    url(r'^article/(?P<id>\d+)$', views.view_article),
    url(r'^article/(?P<pk>\d+)$', views.ReadArticle.as_view(), name='blog_lire'),
    url(r'^(?P<page>\d+)$', views.home),
]
