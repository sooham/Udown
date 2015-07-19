from django.db import models
from tastypie_oauth.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import Authentication
from tastypie_user.models import MyUser as User
from tastypie.exceptions import ImmediateHttpResponse, BadRequest
# Create your models here.

import logging

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from tastypie.authentication import Authentication

from oauth2_provider import oauth2_validators

class StudyGroup(models.Model):
	users = models.ManyToManyField(User, through='Membership')
	description = models.CharField(max_length=140)
	title = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	address = models.CharField(max_length=200)

class Membership(models.Model):
    person = models.ForeignKey(User)
    group = models.ForeignKey(StudyGroup)
    # date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=64)

from tastypie.resources import ModelResource
from tastypie import fields, http
import json

class StudyGroupResource(ModelResource):

	def obj_create(self, bundle, request=None, **kwargs):
		request = bundle.request
		create_type = bundle.data.pop('type')
		key = request.GET.get('oauth_consumer_key')
		user = verify_access_token(key).user

		if(create_type == 'create'):
			new_group = StudyGroup(description = bundle.data.pop('description'))
			new_group.save()
			self.add_user_to_group(user, new_group)
			
			raise ImmediateHttpResponse(http.HttpAccepted(t.user))

		elif(create_type == 'delete'):
			group = StudyGroup.objects.get(id = bundle.data.pop('id'))
			for m in Membership.objects.filter(group = group):
				m.delete()
			group.delete()
			raise ImmediateHttpResponse(http.HttpAccepted())

		elif create_type == 'get_user_groups':
			if(user!=None):
				all_groups = set()
				for m in Membership.objects.filter(person = user):
					all_groups.add(m.group)

				raise ImmediateHttpResponse(http.HttpAccepted(str(list(all_groups))))
			else:
				raise BadRequest('get user group error')

	def add_user_to_group(self, user, group):
		m = Membership(person = user, group = group)
		m.save()

	class Meta:
		queryset = StudyGroup.objects.all()
		resource_name = 'study_group'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class OAuthError(RuntimeError):
    """Generic exception class."""
    def __init__(self, message='OAuth error occured.'):
        self.message = message


from oauth2_provider.models import AccessToken

def verify_access_token(key):
    # Import the AccessToken model
    # try:
    # model = AccessToken
    # model_parts = str(model).split('.')
    # module_path = '.'.join(model_parts[:-1])
    # module = __import__(module_path, globals(), locals(), ['AccessToken'])
    # AccessToken = getattr(module, model_parts[-1])
    # except:
    #     raise OAuthError("Error importing AccessToken model")

    # Check if key is in AccessToken key
    try:
        token = AccessToken.objects.get(token=key)

        # Check if token has expired
        if token.expires < timezone.now():
            raise OAuthError('AccessToken has expired.')
    except AccessToken.DoesNotExist:
        raise OAuthError("AccessToken not found at all.")

    return token
