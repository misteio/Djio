from django.conf.urls import url
from . import views


urlpatterns = [
    # items front
    url(r'^wishlist$', views.get_list, name='wishlist_items_list_front'),

    # categories back
    url(r'^admin/wishlist/category/list$', views.category_list_admin, name='category_list_admin'),
    url(r'^admin/wishlist/category/create$', views.category_create_admin, name='category_create_admin'),
    url(r'^admin/wishlist/category/update/(?P<category_id>[0-9]+)/$', views.category_update_admin, name='category_update_admin'),
    url(r'^admin/wishlist/category/delete/(?P<category_id>[0-9]+)/$', views.category_delete_admin, name='category_delete_admin'),

    # items back
    url(r'^admin/wishlist/item/list$', views.item_list_admin, name='item_list_admin'),
    url(r'^admin/wishlist/item/create$', views.item_create_admin, name='item_create_admin'),
    url(r'^admin/wishlist/item/update/(?P<item_id>[0-9]+)/$', views.item_update_admin, name='item_update_admin'),
    url(r'^admin/wishlist/item/clone/(?P<item_id>[0-9]+)/$', views.item_clone_admin, name='item_clone_admin'),
    url(r'^admin/wishlist/item/revert/(?P<item_id>[0-9]+)/(?P<history_id>[0-9]+)/$', views.item_revert_admin, name='item_revert_admin'),
    url(r'^admin/wishlist/item/delete/(?P<item_id>[0-9]+)/$', views.item_delete_admin, name='item_delete_admin'),
]
