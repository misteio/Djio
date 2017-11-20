from django.apps import AppConfig


class WishlistConfig(AppConfig):
    name = 'wishlist'

    def ready(self):
        import wishlist.signals