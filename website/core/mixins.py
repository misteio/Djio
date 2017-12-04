from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin


class Timestamped(models.Model):
    """
    An abstract behavior representing timestamping a model with``created_at`` and
    ``updated_at`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def changed(self):
        return True if self.updated_at else False

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        return super(Timestamped, self).save(*args, **kwargs)


class Trackable(models.Model):
    created_by = models.ForeignKey(User, related_name='created_%(class)s')
    updated_by = models.ForeignKey(User, related_name='updated_%(class)s')
    class Meta:
        abstract = True


class StaffOnlyMixin(PermissionRequiredMixin):

    '''
    A view mixin that only allows users staff
    '''

    login_url = 'admin:login'
    permission_required = 'is_staff'

