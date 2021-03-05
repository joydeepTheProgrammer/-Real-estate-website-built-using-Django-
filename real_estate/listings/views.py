from django.shortcuts import get_object_or_404, render
from .models import Listings
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .choices import state_choices, bedroom_choices, price_choices
# Create your views here.

def home(request):

    ads = Listings.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(ads, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {

        'ads': paged_listings

    }

    return render(request, 'listings/listings.html', context)



def listing(request, listing_id):

    listing = get_object_or_404(Listings, pk=listing_id)

    context = {

        'listing': listing

    }

    return render(request, 'listings/listing.html', context)



def search(request):

    queryset_list = Listings.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
             queryset_list =  queryset_list.filter(description__icontains=keywords)


    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list =  queryset_list.filter(city__iexact=city)



    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
 
    

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)





    


    context = {

        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


