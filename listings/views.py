from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # order desc on list_date
    # filter using is_published column
    paginator = Paginator(listings, 1)  # we limit listings per page to 1
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    data = {
        'listings': paged_listings,
    }
    # return HttpResponse((len(listings)))
    return render(request, 'listings/listings.html', data)


def listing(request, listing_id):  # passed Id from route
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
