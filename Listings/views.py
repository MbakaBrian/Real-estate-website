from django.shortcuts import render, redirect, get_object_or_404

from Listings.models import Listing
from .forms import ListingForm

def listingsPage(request):
    all_listings = Listing.objects.all
    return render(request,"listingsPage.html",{'all':all_listings})

def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
        else:
            print("Form is not valid")
    else:
        form = ListingForm()

    return render(request, 'create_listing.html', {'form': form})
