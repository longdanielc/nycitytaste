from django.conf.urls import patterns, url
from nycitytasteapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)