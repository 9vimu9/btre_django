from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[0:3]
    # get first 3 listings

    data = {
        'listings': listings
    }

    # return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'pages/index.html', data)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    data = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', data)
