from django.conf.urls import url
from . import views

app_name = 'votetest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/(\d+)/$', views.vote, name='vote'),
    url(r'^addvote/(\d)/$', views.addvote, name='addvote'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
]
