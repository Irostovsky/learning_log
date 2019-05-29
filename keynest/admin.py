# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Key, Store

admin.site.register(Key)
admin.site.register(Store)
