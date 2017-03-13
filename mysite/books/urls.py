from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^display_meta/$', views.display_meta, name='display_meta'),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^', include('django.contrib.auth.urls')),
]