from django.contrib import admin
try:
    from django.conf.urls import patterns, url, include
except ImportError:
    from django.conf.urls.defaults import patterns, url

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r"^admin/", include(admin.site.urls)),)
#    url(r"^js-tests/(?P<path>.*)",
#        'contactBox.views.qunit_view',
#       name='qunit'),)
