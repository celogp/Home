from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
import core.views

urlpatterns = [
	url(r'^$', core.views.login_user, name='login'),
	url(r'^login/', core.views.login_user, name='login'),
	#url(r'^register/', core.views.register_user, name='register'),
	url(r'^home/', core.views.home, name='home'),
	url(r'^cadastros/', core.views.cadastros, name='cadastros'),
	url(r'^pestitulos/', core.views.pestitulos, name='pestitulos'),
	url(r'^frmtitulos/(?P<pk>\d+)$', core.views.frmtitulos, name='frmtitulos'),
	url(r'^admin/', include(admin.site.urls)),
]
