from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^vote/$', views.vote),
    url(r'^detail/$', views.detail),
]
