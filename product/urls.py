from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('/<slug:category_slug>', views.product, name='category_by_product'),
    path('/<slug:category_slug>/<slug:product_slug>', views.product_details, name='product_details'),
]
