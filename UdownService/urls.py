from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from views import index, find, mapme, payment, alert, info, create_study, view_profile
from django.contrib.auth.views import login, logout
from tastypie_user.resources import UserResource
from study_group.models import StudyGroupResource
import notifications

v1_api = Api(api_name='v1')

v1_api.register(UserResource())
v1_api.register(StudyGroupResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UdownService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    
    url(r'^$', index),
    url(r'^accounts/login/$', login),
    url(r'^find/$', find),
    url(r'^find/map$', mapme),
    url(r'^find/hire$', payment),
    url(r'^find/alert$', alert),
    url(r'^find/tutor$', info),
    url(r'^create/group$', create_study),
    url(r'^accounts/view$', view_profile),
    # (r'^accounts/login/$', login),
    # (r'^accounts/logout/$', logout),
    # (r'^accounts/profile/$', profile),
    # (r'^accounts/register/$', register),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    #(r'^inbox/notifications/', include(notifications.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^admin/', include(admin.site.urls)),
)
