from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices
# Create your views here.

def home(request):

    latest_ads = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {

        'latest_ads': latest_ads,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,


    }

    return render(request, 'home.html', context)


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {

        'realtors': realtors,
        'mvp_realtors': mvp_realtors

    }

    return render(request, 'about.html', context)