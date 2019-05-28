# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic, View

from .models import Key


class IndexView(generic.ListView):
    template_name = 'keynest/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Key.objects.order_by('name')


class LoadKeysView(View):
    def get(self, request, *args, **kwargs):
        context = {'message': 'Keys are loaded'}
        return render(request, 'keynest/index.html', context)


