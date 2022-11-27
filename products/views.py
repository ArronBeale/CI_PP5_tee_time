# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
# Internal
from .models import Product, Category
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def all_products(request):
    """ A view to show all products, sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id):
    """ A view to show specific product details """

    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories
    }

    return render(request, 'products/product_detail.html', context)
