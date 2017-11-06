from django.conf.urls import url
from . import views


urlpatterns = [
    # items front
    url(r'^wishlist$', views.get_list, name='wishlist_items_list_front'),

]
