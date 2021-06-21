from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from products.models import Category, Product


# Create your views here.


def ProductViewAll(request):
    fetch_category = Category.objects.all()
    fetch_products = Product.objects.all()
    context = {
        "cat_data": fetch_category,
        "pro_data": fetch_products
    }
    return render(request,template_name='products.html',context=context)


def ProductViewSpecific(request,pid):
    fetch_products = Product.objects.get(pid)
    context = {
        "pro_data" : fetch_products
    }
    return render(request,)

