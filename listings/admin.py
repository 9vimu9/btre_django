from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # we can use list_display to configure what coluns to show in http://127.0.0.1:8000/admin/listings/listing/
    list_display = ('id', 'title', 'is_published', 'realtor', 'list_date', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state')
    list_per_page = 10


admin.site.register(Listing, ListingAdmin)
# admin.site.register(Listing)
# add lising to admin panel
