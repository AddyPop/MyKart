from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def product(request, category_slug=None):
    """categories = None
    products = None"""
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count=products.count()

    data = {
        'products': products,
        'product_count':product_count
    }
    return render(request, 'product.html', context=data)


def product_details(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    data = {
        'single_product':single_product,
    }
    return render(request, 'product_details.html', context=data)