# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.contrib import admin
from django.contrib import admin
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Order, OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid',
    )
    fields = (
        'order_number',
        'user_profile',
        'date',
        'full_name',
        'email',
        'phone_number',
        'address1',
        'address2',
        'town_or_city',
        'postcode',
        'county',
        'country',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid',
    )
    list_display = (
        'order_number',
        'date',
        'full_name',
        'delivery_cost',
        'order_total',
        'grand_total',
    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
