
from django.shortcuts import render
from pathlib import Path

from mainapp.models import Product, ProductCategories

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def index(request):
    content = {'title': 'geekshop Store'}
    return render(request, 'mainapp/index.html', content)


def products(request):

    content = {'title': 'geekshop - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategories.objects.all()
               }
    return render(request, 'mainapp/products.html', content)
