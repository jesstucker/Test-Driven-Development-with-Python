from django.conf.urls import patterns, include, url
from lists import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.home_page, name='home'),
	url(r'^lists/new$', views.new_list, name='new_list'),
	url(r'lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),

    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^superlists/', include('superlists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
