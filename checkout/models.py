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
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Order(models.Model):
    order_number = models.CharField(
        max_length=35,
        null=False,
        editable=False,
        default=''
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    full_name = models.CharField(
        max_length=55,
        null=False,
        blank=False,
        default=''
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        default=''
    )
    address1 = models.CharField(
        max_length=85,
        null=False,
        blank=False,
        default=''
    )
    address2 = models.CharField(
        max_length=85,
        null=True,
        blank=True,
        default=''
    )
    town_or_city = models.CharField(
        max_length=45,
        null=False,
        blank=False,
        default=''
    )
    postcode = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        default=''
    )
    county = models.CharField(
        max_length=85,
        null=True,
        blank=True,
        default=''
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False,
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=True
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
    original_basket = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model for a web order line item
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
        return f'SKU {self.product.code} on order {self.order.order_number}'
