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
from tastypie import http

from tastypie_oauth.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization

from django.utils import timezone

from study_group.models import Membership

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

	# def obj_get_list(self, request=None, **kwargs):
	# 	raise BadRequest('not allowed')

	def obj_create(self, bundle, **kwargs):
		request = bundle.request
		create_type = bundle.data.pop('type')
		try:
			key = request.GET.get('oauth_consumer_key')
			my_user = User.objects.get(username = verify_access_token(key).user.username)
		except OAuthError:
			my_user = None

		if create_type == 'register':

			username = bundle.data.pop('username')
			password1 = bundle.data.pop('password1')
			password2 = bundle.data.pop('password2')
			email = bundle.data.pop('email')

			if (password1 == password2):
				new_user = User.objects.create_user(username, email, password1)
				new_user.save()
				bundle.obj = new_user
				raise ImmediateHttpResponse(http.HttpAccepted())
			else:			
				raise BadRequest('signup error: password did not match')
			# form = USER_CREATION_FORM(bundle.data)
			# if form.is_valid():
			# 	new_user = form.save()
			# 	new_user.send_email('activate')
			# 	bundle.obj = new_user
			# 	raise ImmediateHttpResponse(http.HttpAccepted())
			# 	#auto login, means request twice, first register, then login!
			# else:
			# 	#output the errors for tatstypie
			# 	bundle.errors[self._meta.resource_name] = form.errors
			# 	raise ImmediateHttpResponse(self.error_response(request, bundle.errors))

		elif create_type == 'login':
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

		elif create_type == 'set_gis':
			if my_user:

				my_user.longitude = bundle.data.pop('longitude')
				my_user.latitude = bundle.data.pop('latitude')
				my_user.save()
				raise ImmediateHttpResponse(http.HttpAccepted(my_user.longitude))
			else:
				BadRequest('set user gis info error')

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
		authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

from oauth2_provider.models import AccessToken

class OAuthError(RuntimeError):
    """Generic exception class."""
    def __init__(self, message='OAuth error occured.'):
        self.message = message

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
