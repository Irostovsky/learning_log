# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'keynest/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return []

