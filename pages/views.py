from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_ch,bedroom_ch,state_ch
from django.http import HttpResponse
# Create your views here.

#our view for the home page Develpoed By Mahamoud Salah 
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context={
        'listings':listings,
        'state_ch':state_ch,
        'price_ch':price_ch,
        'bedroom_ch':bedroom_ch
    }
    return render(request,'pages/index.html',context)
#our view for the about page Develpoed By Mahamoud Salah
def about(request):
    realtor_mvp=Realtor.objects.all().filter(is_mvp=True)
    realtors=Realtor.objects.all()

    context={
        'realtor_mvp':realtor_mvp,
        'realtors':realtors,

    }
    return render(request,'pages/about.html',context)

