from django.shortcuts import render, redirect
from store_app . models import *

def BASE(request):
    return render(request,'main/base.html')


def HOME(request):
    product=Product.objects.filter(status='Publish')
    
    context={
        'product': product,
    }
    return render(request,'main/index.html',context)


def PRODUCT(request):
    product=Product.objects.filter(status='Publish')
    categories=Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    color=Color.objects.all()
    brand=Brand.objects.all()
    
    CATID=request.GET.get("categories")
    if CATID:
        product=Product.objects.filter(categories_=_CATID)
    else:
        product=Product.objects.filter(status='Publish')
    context={
        'product': product,
        'categories':categories,
        'filter_price':filter_price,
        'color': color,
        'brand' : brand
    }
    
    return render(request,'main/product.html',context)