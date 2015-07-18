from django.db import models
from tastypie_user.models import MyUser as User
# Create your models here.

class StudyGroup(models.Model):
	users = models.ManyToManyField(User)
	description = models.CharField(max_length = 140)

# class Membership(models.Model):
#     person = models.ForeignKey(User)
#     group = models.ForeignKey(StudyGroup)
#     # date_joined = models.DateField()
#     # invite_reason = models.CharField(max_length=64)

from tastypie.resources import ModelResource
from tastypie import fields, http
import json

class StudyGroupResource(ModelResource):

	def obj_create(self, bundle, request=None, **kwargs):
		request = bundle.request
		create_type = bundle.data.pop('type')
		# if create_type == 'upload':
		# 	user_id = bundle.data.pop('user')
		# 	user = Subject.objects.get(id=user_id)

		# 	glucose = bundle.data.pop('glucose')
		# 	diet = bundle.data.pop('diet')
		# 	exercise = bundle.data.pop('exercise')
			
		# 	upload_data = DailyData(user=user, glucose=glucose, diet=diet, exercise=exercise)
		# 	upload_data.save()
		# 	raise ImmediateHttpResponse(http.HttpAccepted())
                

	class Meta:
		queryset = StudyGroup.objects.all()
		resource_name = 'study_group'
