from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_tut.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sobre-mi/', TemplateView.as_view(template_name="sobre-mi.html"), name="about"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    url('^', include('django.contrib.auth.urls')),
]
