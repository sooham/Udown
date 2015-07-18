from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
<<<<<<< HEAD
from views import profile, register
=======
from views import profile
>>>>>>> 6a5c61a4018685548cadb2db6515d7bd1abe3fc8
from django.contrib.auth.views import login, logout
from tastypie_user.resources import UserResource
import notifications

v1_api = Api(api_name='v1')

v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UdownService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    

    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
<<<<<<< HEAD
    (r'^accounts/register/$', register),

    #url(r'^inbox/notifications/', include(notifications.urls)),
=======

    url(r'^inbox/notifications/', include(notifications.urls)),
>>>>>>> 6a5c61a4018685548cadb2db6515d7bd1abe3fc8

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
