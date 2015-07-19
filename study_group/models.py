from django.db import models
from tastypie_oauth.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie_user.models import MyUser as User
from tastypie.exceptions import ImmediateHttpResponse, BadRequest
# Create your models here.

class StudyGroup(models.Model):
	users = models.ManyToManyField(User, through='Membership')
	description = models.CharField(max_length = 140)

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
		if(create_type == 'create'):
			new_group = StudyGroup(description = bundle.data.pop('description'))
			new_group.save()
			add_user_to_group(request.user, new_group)
			raise ImmediateHttpResponse(http.HttpAccepted())

		elif(create_type == 'delete'):
			group = StudyGroup.objects.get(id = bundle.data.pop('id'))
			for m in Membership.objects.filter(group = group):
				m.delete()
			group.delete()
			raise ImmediateHttpResponse(http.HttpAccepted())

	def add_user_to_group(user, group):
		m = Membership(person = user, group = group)
		m.save()


	class Meta:
		queryset = StudyGroup.objects.all()
		resource_name = 'study_group'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
