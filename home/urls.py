from django.contrib import admin
from django.urls import path
from . import views

#Django Admin customization
admin.site.site_header = "KnowledgeForYou Admin Portal"
admin.site.site_title = "Welcome to KnowledgeForYou Admin"
admin.site.index_title = "Welcome to Abhinav's site admin portal"

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('privacypolicy', views.privacy, name="privacy"),
    path('search', views.search, name="search")
]