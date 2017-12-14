from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # Admin
    url(r'^admin/account/password/change$', views.admin_password_change, name='admin_user_password_change'),
    url(r'^admin/ckupload', csrf_exempt(views.ckupload_service), name='admin_ckeditor_upload'),
    url(r'^admin/editor', views.admin_editor_html, name='admin_ckeditor_upload'),
    url(r'^admin/account/profile/edit$', views.admin_edit_profile, name='admin_user_profile_edit'),

    #Front
    url(r'^login', views.front_login, name='front_user_login'),
    url(r'^logout', views.front_logout, name='front_user_logout'),
    url(r'^signup', views.front_signup, name='front_user_signup'),
    url(r'^account/profile-edit$', views.front_edit_profile, name='front_user_profile_edit'),

    #Menu
    url(r'^admin/menu/list$', views.menu_list_admin, name='menu_list_admin'),
    url(r'^admin/menu/create$', views.menu_create_admin, name='menu_create_admin'),
    url(r'^admin/menu/update/(?P<menu_id>[0-9]+)/$', views.menu_update_admin, name='menu_update_admin'),
    url(r'^admin/menu/delete/(?P<menu_id>[0-9]+)/$', views.menu_delete_admin, name='menu_delete_admin'),
    url(r'^admin/menu/move/(?P<node_from_id>[0-9]+)/(?P<node_to_id>[0-9]+)/(?P<action>[-\w]+)/$', views.ajax_menu_move, name='menu_move_ajax_admin'),

]
