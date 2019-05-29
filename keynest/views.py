# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic, View
from django.shortcuts import redirect, reverse

from .models import Key, Store
from .services import load_keys, load_stores

from django.conf import settings


class IndexView(generic.ListView):
    model = Key
    template_name = 'keynest/index.html'

    def get_queryset(self):
        return Key.objects.all().order_by('name')


class StoreListView(generic.ListView):
    model = Store

    def get_queryset(self):
        return Store.objects.all().order_by('name')


class LoadKeysView(View):
    def get(self, request, *args, **kwargs):
        load_stores(settings.KEYNEST_API_KEY)
        load_keys(settings.KEYNEST_API_KEY)
        return redirect(reverse('keynest:index'))

