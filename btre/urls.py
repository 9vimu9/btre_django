from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),  # works like prefix for pages URLs
    path('admin/', admin.site.urls),
]
