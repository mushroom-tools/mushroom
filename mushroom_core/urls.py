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
	url(r'^browse/(.+)?$', 'browse.views.browse_page'),
	url(r'^confcall/$', 'dashboard.views.confcall'),
	url(r'^issue/$', 'issues.views.issues_page'),
	url(r'^issue/(\w+)/$', 'issues.views.issue_page'),
	url(r'^issue_create/$', 'issues.views.issue_create_page'),
	url(r'^issue_close/(\w+)/$', 'issues.views.issue_close_page'),
	url(r'^issue_reopen/(\w+)/$', 'issues.views.issue_reopen_page'),
	url(r'^issue_delete/(\w+)/$', 'issues.views.issue_delete_page'),
	url(r'^issue_edit/(\w+)/$', 'issues.views.issue_edit_page'),
    # Examples:
    # url(r'^$', 'mushroom_core.views.home', name='home'),
    # url(r'^mushroom_core/', include('mushroom_core.foo.urls')),
)
