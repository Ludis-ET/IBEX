# signals.py
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from .models import Checkout

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == ST_PP_COMPLETED:
        try:
            checkout = Checkout.objects.get(paypal_transaction_id=ipn.invoice)
            checkout.status = 'COMPLETED'
            checkout.save()
        except Checkout.DoesNotExist:
            pass
    else:
        try:
            checkout = Checkout.objects.get(paypal_transaction_id=ipn.invoice)
            checkout.status = 'FAILED'
            checkout.save()
        except Checkout.DoesNotExist:
            pass
