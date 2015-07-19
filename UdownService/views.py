from django.shortcuts import render_to_response
from twilio.rest import TwilioRestClient
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render_to_response('index.html')

def find(request):
    return render_to_response('find.html')
def mapme(request):
    return render_to_response('map.html')
def payment(request):
	return render_to_response('payment.html')
def alert(request):
	# Find these values at https://twilio.com/user/account
	account_sid = "ACc6ddee70e1d4f0e323614b1093968848"
	auth_token = "ee55744af15af596f7be3b1e66fb5cb2"
	client = TwilioRestClient(account_sid, auth_token)
	 
	message = client.messages.create(to="+16478645896", from_="+1289 2120994", body="A friend has invited you to a study session! Tap here to accept")

	return render_to_response('alert.html')
def info(request):
	return render_to_response('info.html')
def create_study(request):
	return render_to_response('study.html');
def view_profile(request):
	return render_to_response('view.html')

# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('/account/logedin/')
#     else:
#         return HttpResponseRedirect('/account/invalid/')

# def profile(request):
#     return render_to_response('registration/profile.html', {'username':request.user.username, 'user':request.user})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return HttpResponseRedirect('/accounts/signup/success/')
#     else:
#         form = UserCreationForm()
#     return render_to_response("registration/register.html", {
#         'form': form,
#     }, RequestContext(request))

# def signup_success(request):
#     return render_to_response('registration/signup_success.html')

# def invite(request):
#     return render_to_response('invite.html');

# def home(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return HttpResponseRedirect('/accounts/profile/')
#     else:
#         form = UserCreationForm()
#     return render_to_response('index.html', {
#         'form': form,
#     }, RequestContext(request))
