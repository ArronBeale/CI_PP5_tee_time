# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.shortcuts import (render, redirect, reverse, get_object_or_404,
                              HttpResponse
                              )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
import json
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, Category
from basket.contexts import basket_contents
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
