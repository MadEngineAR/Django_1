import json
import os
from django.shortcuts import render
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def index(request):
    content = {'title': 'geekshop Store'}
    return render(request, 'mainapp/index.html', content)


def products(request):
    file_path_products = os.path.join(BASE_DIR, 'mainapp/fixtures/products.json')
    file_path_categories = os.path.join(BASE_DIR, 'mainapp/fixtures/categories.json')
    content = {'title': 'geekshop - Каталог',
               'products': json.load(open(file_path_products, encoding='UTF-8')),
               'categories': json.load(open(file_path_categories, encoding='UTF-8'))
               }
    return render(request, 'mainapp/products.html', content)
