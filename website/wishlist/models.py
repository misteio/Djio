from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from core.mixins import Timestamped
from simple_history.models import HistoricalRecords
from django.db import models
from .managers import PublishedManager, LazyLoadAuthorManager
from ordered_model.models import OrderedModel
from mptt.models import MPTTModel, TreeForeignKey


class Category(Timestamped, MPTTModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    description = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    history = HistoricalRecords(excluded_fields=['rght', 'level', 'lft', 'tree_id'])

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i + 1]))
        return slugs


class Item(Timestamped, OrderedModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    complete_slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, related_name='whislist_items')
    category = models.ForeignKey(Category, related_name='category_items', blank=True)
    body = models.TextField()
    resume = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    image_field = models.ImageField(upload_to="item/", blank=True)
    url = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    participate = models.ManyToManyField(User, blank=True)
    multi_participate = models.BooleanField(default=False)

    history = HistoricalRecords()

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.
    admin_load = LazyLoadAuthorManager()  # The Dahl-specific manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
