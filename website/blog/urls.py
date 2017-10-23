from django.conf.urls import url
from . import views


urlpatterns = [
    # post admin
    url(r'^admin/blog$', views.post_list_admin, name='post_list_admin'),
    url(r'^admin/blog/create$', views.post_form_admin, name='post_create_admin'),
    url(r'^admin/blog/update/(?P<post_id>[0-9]+)/$', views.post_update_admin, name='post_update_admin'),
    url(r'^admin/blog/clone/(?P<post_id>[0-9]+)/$', views.post_clone_admin, name='post_clone_admin'),
    url(r'^admin/blog/delete/(?P<post_id>[0-9]+)/$', views.post_delete_admin, name='post_delete_admin'),

    # post front
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
