from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('pages.urls')),  # works like prefix for pages URLs
                  path('listings/', include('listings.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # add media related URLS
