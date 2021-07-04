from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),  # /listings
    # we add prefix for every app. here it would be listings . so complete URL is /listings
    path('<int:listing_id>', views.listing, name='listing'),  # /listings/12
    path('search', views.search, name='search')  # listings/search
]
