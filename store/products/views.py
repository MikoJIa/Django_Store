from django.shortcuts import render
from django.http import HttpResponse
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'STORE',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
