from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .mixins import Timestamped
from mptt.models import MPTTModel, TreeForeignKey


class Profile(Timestamped):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    city = models.CharField(max_length=100, validators=[MinLengthValidator(4)], blank=True,null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=250, validators=[MinLengthValidator(20)], blank=True,null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created_at', )


class Menu(Timestamped, MPTTModel):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(4)])
    url = models.CharField(max_length=255, blank=True, null=True)
    mapping = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        ordering = ('lft', 'tree_id')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title