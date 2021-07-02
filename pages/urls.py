from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # can use name param to set name for url
    path('about', views.about, name='about')
]
