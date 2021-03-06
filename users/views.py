# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate

from forms import CustomUserCreationForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """Register the new user"""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        print(request.POST)
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
