from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/account/logedin/')
    else:
        return HttpResponseRedirect('/account/invalid/')

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/pnf/")

def profile(request):
    return render_to_response('registration/profile.html', {'username':request.user.username, 'user':request.user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/accounts/signup/success/')
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, RequestContext(request))

def signup_success(request):
    return render_to_response('registration/signup_success.html')

def invite(request):
    return render_to_response('invite.html');

def home(request):
    return render_to_response('index.html');
