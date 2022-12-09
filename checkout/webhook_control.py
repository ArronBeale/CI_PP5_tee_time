# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import json
import time
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Order, OrderLineItem
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# From CI Boutique Ado webhook handler
class StripeWebHook_Handler:
    """
    Handle webhook for Stripe
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send confirmation email to user
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',

            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle webhook event of generic, unknown, unexpected
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the webhook from Stripe for payment_intent.succeeded
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        # updated
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        # updated
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile info if save_info
        # profile = None
        # username = intent.metadata.username
        # if username != 'AnonymousUser':
        #     profile = UserProfile.objects.get(user__username=username)
        #     if save_info:
        #         profile.default_phone_number = shipping_details.phone
        #         profile.default_country = shipping_details.address.country
        #         profile.default_postcode = shipping_details.address.postal_code
        #         profile.default_town_or_city = shipping_details.address.city
        #         profile.default_address1 = shipping_details.address.line1
        #         profile.default_address2 = shipping_details.address.line2
        #         profile.default_county = shipping_details.address.state
        #         profile.save()

        order_exists = False
        attempt = 1
        # While loop makes 5 attempts to check if order was created
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                # break out of loop if order
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            # if order, return 200 response
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS:\
                     Verified order already in database',
                status=200)
        else:
            # creates a new order
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items(
                        ):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    # deletes order if error and return 500 error response
                    # to stripe
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # if the order has been created by the webhook handler
        # the email is sent after the order was created
        self._send_confirmation_email(order)
        # returns status 200 response
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created\
                 order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the webhook from Stripe for payment_intent.payment_failed
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
