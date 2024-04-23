from django.urls import path
from .views import Home, Search
from . import views

urlpatterns = [

    path('search/', Search.as_view(), name='search'),
    path('', views.Home, name='home'),
    path('about-us', views.about,  name='about'),
    path('create', views.create, name='create'),
    path('admin', views.admin, name='admin'),
]
