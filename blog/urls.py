from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$',views.new, name="new_post"),    
    url(r'^(?P<id>\d+)/$', views.show),
    url(r'^(?P<id>\d+)/edit/$', views.update),
    url(r'^(?P<id>\d+)/delete/$', views.delete)
]