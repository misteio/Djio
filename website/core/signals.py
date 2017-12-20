from django.db.models.signals import pre_save
from django.dispatch import receiver
from .mixins import Trackable
from compressor.signals import post_compress
from constance import config


@receiver(pre_save)
def security_attributes(sender, instance, **kwargs):
    if not issubclass(sender, Trackable):
        return


@receiver(post_compress)
def post_compress_front(sender, type, mode, context, **kwargs):
    if context['compressed']['name'] == 'front_css':
        config.CSS_FRONT_COMPRESSED = context['compressed']['url']

    if context['compressed']['name'] == 'front_js':
        config.JS_FRONT_COMPRESSED = context['compressed']['url']