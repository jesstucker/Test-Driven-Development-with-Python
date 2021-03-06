from django.conf.urls import patterns, include, url
from lists import views as list_views
from lists import urls as list_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', list_views.home_page, name='home'),
	url(r'^lists/', include(list_urls)),
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^superlists/', include('superlists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
