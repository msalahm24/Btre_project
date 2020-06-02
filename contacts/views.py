from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(requst):
    if requst.method=='POST':
        user_id=requst.POST['user_id']
        realtor_email=requst.POST['realtor_email']
        listing_id=requst.POST['listing_id']
        listing=requst.POST['listing']
        name=requst.POST['name']
        user_email=requst.POST['email']
        user_phone=requst.POST['phone']
        user_message=requst.POST['message']
        if requst.user.is_authenticated:
            user_id=requst.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(requst,'you have already made inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact=Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=user_email,
            message=user_message,
            phone=user_phone,
            user_id=user_id
        )
        contact.save()
        send_mail(
            'property listing inquiry',
            'ther is an inquiry for the listin '+listing + '  more info open your admin',
            'test245server@gmail.com',
            [realtor_email],
            fail_silently=False,
        )
        messages.success(requst,'your request is now with the realtor ')
        return redirect('/listings/'+listing_id)


