from django.db import models


class ListAdminManager(models.Manager):
    def get_queryset(self):
        return super(ListAdminManager, self).get_queryset().select_related('author')