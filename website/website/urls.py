from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.i18n import javascript_catalog
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

js_info_dict = {
    'packages': ('your.app.package',),
}

urlpatterns = [
    url(r'^', include('core.urls', namespace='core', app_name='core')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^', include('wishlist.urls', namespace='wishlist', app_name='wishlist')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    url(r'^admin/roxyfileman/', include('roxyfileman.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += url(r'^', include('page.urls', namespace='page', app_name='page')),



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


