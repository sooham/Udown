from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from views import profile
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

    url(r'^inbox/notifications/', include(notifications.urls)),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
