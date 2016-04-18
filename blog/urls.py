from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^posts/(?P<pk>[0-9]+)/edit$', views.PostEdit.as_view(), name='post_edit'),
    url(r'^posts/(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(), name='post_delete'),
]