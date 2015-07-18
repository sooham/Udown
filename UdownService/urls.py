from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from views import profile, register, home
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

    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
    (r'^accounts/register/$', register),

    (r'', home),

    #(r'^inbox/notifications/', include(notifications.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^admin/', include(admin.site.urls)),
)
