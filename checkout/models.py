# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Order(models.Model):
    order_number = models.CharField(
        max_length=35,
        null=False,
        editable=False
    )
    full_name = models.CharField(
        max_length=55,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    address1 = models.CharField(
        max_length=85,
        null=False,
        blank=False
    )
    address2 = models.CharField(
        max_length=85,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=45,
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    county = models.CharField(
        max_length=85,
        null=True,
        blank=True
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
    )
    date = models.DateTimeField(
        auto_now_add=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='')


class OrderLineItem(models.Model):
    """
    A model for a website order line item
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    product_size = models.CharField(
        max_length=2,
        null=True,
        blank=True
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
