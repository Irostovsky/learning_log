# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic, View
from django.shortcuts import redirect, reverse

from .models import Key
from .services import load_keys


class IndexView(generic.ListView):
    model = Key
    template_name = 'keynest/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Key.objects.all().order_by('name')


class LoadKeysView(View):
    def get(self, request, *args, **kwargs):
        load_keys()
        return redirect(reverse('keynest:index'))


