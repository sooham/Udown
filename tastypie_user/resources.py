try:
    import json
except ImportError:
	from django.utils import simplejson as json
from tastypie.resources import ModelResource
from tastypie.exceptions import ImmediateHttpResponse, BadRequest
from tastypie_user.models import MyUser as User
from django.contrib import auth
from django.conf import settings
from django.http import HttpResponse

class UserResource(ModelResource):

	def show_keys(self, request):
		if request.user.is_authenticated():
			#api_key = request.user.api_key.key
			keys = {
				'username': request.user.username,
				#'api_key': api_key,
				'session_name': settings.SESSION_COOKIE_NAME,
				'session_key': request.session.session_key}
			raise ImmediateHttpResponse(
				HttpResponse(json.dumps(keys), content_type='application/json')
			)
		else:
			raise BadRequest('not login')

	def obj_get_list(self, request=None, **kwargs):
		raise BadRequest('not allowed')

	def obj_create(self, bundle, **kwargs):
		request = bundle.request
		create_type = bundle.data.pop('type')
		if create_type == 'login':
			expiry_seconds = bundle.data.pop('expiry_seconds', None)
			user = auth.authenticate(**bundle.data)

			if user is not None and user.is_active:
				auth.login(request, user)
				if expiry_seconds:
					request.session.set_expiry(int(expiry_seconds))
				self.show_keys(request)
			elif user is not None and not user.is_active:
				raise BadRequest('not active')
			else:
				raise BadRequest('login error')

		else:
			raise BadRequest('create user resource error')


	def get_detail(self, request=None, **kwargs):
		if kwargs.get('pk') == 'keys':
			self.show_keys(request)
		else:
			return super(UserResource, self).get_detail(request, **kwargs)


   	def dehydrate(self, bundle):
		bundle.data['email'] = ''
		bundle.data['password'] = ''
		return bundle

	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
