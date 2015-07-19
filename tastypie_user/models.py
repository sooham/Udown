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

	degree = models.CharField(max_length=2,
		choices=DEGREE_CHOICES,
		default='HS')
	pass

class TutorUser(MyUser):
	pass

class StudentUser(MyUser):
	pass
