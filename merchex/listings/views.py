from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Je suis un paragraph test</p>')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', context={'listings': listings})


def contact(request):
    return render(request, 'listings/contact.html', context={})