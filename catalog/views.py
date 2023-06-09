from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # Викониэм запити до БД и отримуэм необхидни дани
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_producers = Producer.objects.all()

    # Передаємо далі використовуючи контекстний словник
    return render(request, 'catalog/index.html', context={
        'title': 'Каталог',
        'page': 'index',
        'app': 'catalog',
        'all_products': all_products,
        'all_categories': all_categories,
        'all_producers': all_producers
    })