from django.db.models.signals import pre_save
from django.dispatch import receiver
from.models import Post
"""
create slug for having complete url
"""


@receiver(pre_save, sender=Post)
def tree_complete_slug(sender, instance, **kwargs):
    slug = ''
    for category in instance.category.get_ancestors():
       slug += '/' + category.slug
    slug += instance.category.slug + '/' + instance.slug

    instance.complete_slug = slug
