from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Item
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
import requests
import os


@receiver(pre_save, sender=Item)
def item_save_image_field(sender, instance, *args, **kwargs):
    img_temp = NamedTemporaryFile(delete=True)
    if "http" not in instance.image:
        response = requests.get(settings.MEDIA_HOST + instance.image)
    else:
        response = requests.get(instance.image)

    img_temp.write(response.content)
    img_temp.flush()
    file = File(img_temp)
    extension = os.path.splitext(instance.image)[1]
    instance.image_field.save(instance.slug + extension, file, False)