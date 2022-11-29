# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.shortcuts import render
from products.models import Product, Category
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_basket(request):
    """
    a view to display the basket page
    """
    products = Product.objects.all()
    categories_list = Category.objects.all()

    context = {
        'products': products,
        'categories_list': categories_list
               }
    return render(request, 'basket/basket.html', context)
