from django.conf.urls import url
from . import views


urlpatterns = [
    # categories back
    url(r'^admin/page/category/list$', views.category_list_admin, name='category_list_admin'),
    url(r'^admin/page/category/create$', views.category_create_admin, name='category_create_admin'),
    url(r'^admin/page/category/create/ajax$', views.ajax_category_save, name='category_create_admin_ajax'),
    url(r'^admin/page/category/update/(?P<category_id>[0-9]+)/$', views.category_update_admin, name='category_update_admin'),
    url(r'^admin/page/category/delete/(?P<category_id>[0-9]+)/$', views.category_delete_admin, name='category_delete_admin'),
    url(r'^admin/page/category/move/(?P<node_from_id>[0-9]+)/(?P<node_to_id>[0-9]+)/(?P<action>[-\w]+)/$', views.ajax_category_move, name='category_move_ajax_admin'),
    url(r'^admin/page/category/revert/(?P<category_id>[0-9]+)/(?P<history_id>[0-9]+)/$', views.category_revert_admin, name='category_revert_admin'),


    # posts back
    url(r'^admin/page/post/list$', views.PostListView.as_view(), name='post_list_admin'),
    url(r'^admin/page/post/create$', views.PostCreateView.as_view(), name='post_create_admin'),
    url(r'^admin/page/post/update/(?P<post_id>[0-9]+)/$', views.post_update_admin, name='post_update_admin'),
    url(r'^admin/page/post/clone/(?P<post_id>[0-9]+)/$', views.post_clone_admin, name='post_clone_admin'),
    url(r'^admin/page/post/revert/(?P<post_id>[0-9]+)/(?P<history_id>[0-9]+)/$', views.post_revert_admin, name='post_revert_admin'),
    url(r'^admin/page/post/restore/(?P<history_id>[0-9]+)/$', views.post_restore_admin, name='post_restore_admin'),
    url(r'^admin/page/post/delete/(?P<post_id>[0-9]+)/$', views.post_delete_admin, name='post_delete_admin'),
    url(r'^admin/page/post/swap/(?P<post_id>[0-9]+)/(?P<position>[0-9]+)/$', views.post_swap_position_admin, name='post_swap_position_admin'),

    # config back
    url(r'^admin/page/config/header$', views.config_header_admin, name='config_page_header_admin'),
    url(r'^admin/page/config/footer$', views.config_footer_admin, name='config_page_footer_admin'),

    # pages front
    #url(r'^(?P<category_slug>[-\w]+)/(?P<page_slug>[-\w]+)$', views.page_post_list_category, name='post_list_category_front'),
    url(r'^(?P<post_slug>[-\w]+)$', views.post_detail, name='page_post_detail_front'),
    url(r'^$', views.home_page, name='page_post_home_front'),
]
