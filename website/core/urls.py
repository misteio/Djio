from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # Admin
    url(r'^admin/password-change$', views.admin_password_change, name='admin_user_password_change'),
    url(r'^admin/ckupload', csrf_exempt(views.ckupload_service), name='admin_ckeditor_upload'),
    url(r'^admin/editor', views.admin_editor_html, name='admin_ckeditor_upload'),

    #Front
    url(r'^login', views.front_login, name='front_user_login'),
    url(r'^logout', views.front_logout, name='front_user_logout'),
    url(r'^signup', views.front_signup, name='front_user_signup'),
    url(r'^account/profile-edit$', views.front_edit_profile, name='front_user_profile_edit'),
]
