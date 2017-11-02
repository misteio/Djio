from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from core.mixins import Timestamped
from simple_history.models import HistoricalRecords
from django.db import models
from .managers import PublishedManager, LazyLoadAuthorManager


class Post(Timestamped):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    resume = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    history = HistoricalRecords()

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.
    admin_load = LazyLoadAuthorManager()  # The Dahl-specific manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])