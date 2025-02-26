from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.form import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', context={'band': band})

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Je suis un paragraph test</p>')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', context={'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', context={'listing': listing})

def contact(request):
    return render(request, 'listings/contact.html', context={})

def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx contact Us Form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-sent')
            
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', context={'form': form})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('band-list')
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})
    

def email_sent(request):
    return render(request, 'listings/email_sent.html')
