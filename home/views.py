# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.shortcuts import render
from products.models import Product, Category
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home(request):
    """
    a view to display the homepage
    """
    products = Product.objects.all()
    categories_list = Category.objects.all()

    context = {
        'products': products,
        'categories_list': categories_list
               }
    return render(request, 'home/index.html', context)
