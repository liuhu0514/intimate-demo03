from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^vote/(\d+)/$', views.vote),
    url(r'^addvote/(\d)/$', views.addvote),
    url(r'^detail/(\d+)/$', views.detail),
]
