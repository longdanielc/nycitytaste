from django.conf.urls import patterns, include, url
from django.contrib import admin
from nycitytasteapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nycitytaste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('nycitytasteapp.urls')),
    url(r'^nycitytasteapp/', include('nycitytasteapp.urls')),

)
