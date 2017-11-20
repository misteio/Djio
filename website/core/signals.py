from django.db.models.signals import pre_save
from django.dispatch import receiver
from .mixins import Trackable


@receiver(pre_save)
def security_attributes(sender, instance, **kwargs):
    if not issubclass(sender, Trackable):
        return