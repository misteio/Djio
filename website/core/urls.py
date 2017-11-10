from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # post views
    url(r'^admin/password-change$', views.password_change, name='admin_user_password_change'),
    url(r'^admin/ckupload', csrf_exempt(views.ckupload_service), name='admin_ckeditor_upload'),
    url(r'^admin/editor', views.editor_html, name='admin_ckeditor_upload'),
]
