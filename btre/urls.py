from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),  # works like prefix for pages URLs
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
