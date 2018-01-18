# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.forms import RegisterModelForm
from first_app.models import RegisterModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse

# Create your views here.

def main(request):
    d_return = {'templated_tag': 'I came from a templated tag!'}
    #return HttpResponse('Hello from first_app main view')
    return render(request, 'first_app/main.html', context=d_return)

@login_required
def RegisteredUsersView(request):
    reg_users = RegisterModel.objects.order_by('email')
    d_users = {'users':reg_users}
    return render(request, 'first_app/registers.html', context=d_users)

@login_required
def UserLogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

def RegisterView(request):
    form = UserModelForm()

    if request.method == 'POST':
        form = RegisterModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return main(request)
        else:
            print 'ERROR'

    return render(request, r'first_app/register_user.html', {'form': form})

def UserLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                print "ACCOUNT NOT ACTIVE"
        else:
            print "PLEASE REGISTER FIRST"
    else:
        return render(request, 'first_app/user_login.html', {})
