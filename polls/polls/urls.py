from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from poll.views import pollWeb,submit

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'polls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pollWeb/$',pollWeb),
    url(r'^submit/$',submit),
)
