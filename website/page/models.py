from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from core.mixins import Timestamped
from simple_history.models import HistoricalRecords
from django.db import models
from ordered_model.models import OrderedModel
from mptt.models import MPTTModel, TreeForeignKey
from .managers import ListAdminManager


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

    history = HistoricalRecords(excluded_fields=['rght', 'level', 'lft', 'tree_id', 'parent_id'])

    # Managers
    objects = models.Manager()  # The default manager.

    class Meta:
        ordering = ('lft', 'tree_id')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['slug']


class Post(Timestamped, OrderedModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    complete_slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='page_posts')
    category = models.ForeignKey(Category, related_name='category_posts', blank=True)
    body = models.TextField()
    resume = models.TextField()
    image = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    image_field = models.ImageField(upload_to="page/", blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    history = HistoricalRecords()

    # Managers
    objects = models.Manager()  # The default manager.
    admin = ListAdminManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
