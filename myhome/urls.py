from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import core.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myhome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.home, name='home'),
    url(r'^home/', core.views.home, name='home'),
]
