from django.conf.urls import url
from . import views

app_name = 'votetest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/(\d+)/$', views.vote, name='vote'),
    url(r'^addvote/(\d)/$', views.addvote, name='addvote'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^editres/(\d+)/$', views.editres, name='editres'),
    url(r'^add/$', views.add, name='add'),
    url(r'^addres$', views.addres, name='addres'),
]
