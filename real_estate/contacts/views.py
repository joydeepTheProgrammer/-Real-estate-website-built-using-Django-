from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listings_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if user has an enquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listings_id=listings_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listings_id)
        contact = Contact(listing=listing, listings_id=listings_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        #Send mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an Inquiry for '+ listing +'.Sign into the admin panel for more info',
            'joydeepmajumdar1994@gmail.com',
            [realtor_email, 'joydeepmajumdar2016@gmail.com'],
            fail_silently=False

        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listings_id)
