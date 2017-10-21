from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^admin/password-change$', views.post_list, name='admin_user_password_change'),
]
