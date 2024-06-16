from django.shortcuts import render
from .models import Product

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Ecommerce_App/products_list.html', context)
