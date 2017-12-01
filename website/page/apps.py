from django.apps import AppConfig


class PageConfig(AppConfig):
    name = 'page'

    def ready(self):
        import page.signals