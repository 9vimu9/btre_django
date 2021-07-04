from django.shortcuts import render
from .models import Listing
from django.http import HttpResponse


def index(request):
    listings = Listing.objects.all()
    data = {
        'listings': listings,
        'id': 5
    }
    # return HttpResponse((len(listings)))
    return render(request, 'listings/listings.html', data)


def listing(request, listing_id):  # passed Id from route
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
