from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all()
    data = {
        'products':products
    }
    return render(request, 'home.html', context=data)