from django.http import request
from django.shortcuts import render
from .models import LandingPageDetails
# Create your views here.

def HomePage(request, pk):
    obj = LandingPageDetails.objects.filter(id=pk)[0]
    discount =obj.actuallPrice-((obj.actuallPrice * obj.percentage)/100)
    # import pdb;pdb.set_trace()
    return render(request, "index.html",{'data': obj, 'discount':discount})

def HomePage1(request):
    # obj = LandingPageDetails.objects.all()[0]
    return render(request, "index.html")