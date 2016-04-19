from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^posts/(?P<pk>[0-9]+)/edit$', views.PostEdit.as_view(), name='post_edit'),
    url(r'^posts/(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^posts/(?P<post_pk>[0-9]+)/comments/(?P<comment_pk>[0-9]+)/like$', views.comment_like, name='comment_like'),
    url(r'^posts/(?P<post_pk>[0-9]+)/comments/(?P<comment_pk>[0-9]+)/dislike$', views.comment_dislike, name='comment_dislike'),
]