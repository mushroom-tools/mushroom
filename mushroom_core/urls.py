from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'main.views.main_page'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'main.views.logout_page'),
	url(r'^join_member/$', 'join_member.views.join_member_page'),
	url(r'^dashboard/$', 'dashboard.views.dashboard_page'),
	url(r'^timeline/$', 'timeline.views.timeline_page'),
	url(r'^browse/$', 'browse.views.browse_page'),
	url(r'^confcall/$', 'dashboard.views.confcall'),
    # Examples:
    # url(r'^$', 'mushroom_core.views.home', name='home'),
    # url(r'^mushroom_core/', include('mushroom_core.foo.urls')),
)
