import abc
import stripe
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

stripe.api_key = settings.STRIPE_SECRET_KEY


class BaseStripeModel(TimeStampedModel):
    """An abstract base class model for all Stripe models."""
    stripe_id = models.CharField(_('stripe ID'), max_length=255, primary_key=True)

    class Meta:
        abstract = True

    @property
    @abc.abstractmethod
    def stripe_object(self):
        pass


class StripeCustomer(BaseStripeModel):
    """Stripe customer object reference."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stripe_customer',
        verbose_name=_('user'))

    @property
    def stripe_object(self):
        return stripe.Customer.retrieve(self.stripe_id)


class StripeCreditCard(BaseStripeModel):
    """Stripe credit card object reference."""
    stripe_customer = models.ForeignKey('payments.StripeCustomer', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="credit_cards", verbose_name=_('stripe customer'))

    fingerprint = models.CharField(_('fingerprint'), max_length=16)

    @property
    def stripe_object(self):
        return stripe.Card.retrieve(self.stripe_id)
