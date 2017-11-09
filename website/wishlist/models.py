from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from core.mixins import Timestamped
from simple_history.models import HistoricalRecords
from django.db import models
from .managers import PublishedManager, LazyLoadAuthorManager


class Category(Timestamped):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    description = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    history = HistoricalRecords()

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


class Item(Timestamped):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='whislist_items')
    category = models.ForeignKey(Category, related_name='category_items', blank=True)
    body = models.TextField()
    resume = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    url = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    participate = models.ManyToManyField(User, blank=True)

    history = HistoricalRecords()

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.
    admin_load = LazyLoadAuthorManager()  # The Dahl-specific manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
