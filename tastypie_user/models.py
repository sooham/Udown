import warnings
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class MyUser(User):

	DEGREE_CHOICES = (
		('HS', 'highschool'),
		('UG', 'undergrad'),
		('GR', 'grad'),
		('PD', 'PhD'),
	)

	longitude = models.FloatField(default = 0)
	latitude = models.FloatField(default = 0)
	number = models.CharField(max_length = 15)
	area_of_study = models.CharField(max_length=100)
	degree = models.CharField(max_length=2,
		choices=DEGREE_CHOICES,
		default='HS')

class TutorUser(MyUser):
	pass

class StudentUser(MyUser):
	pass
