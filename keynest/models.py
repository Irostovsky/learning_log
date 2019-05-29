# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    store_time = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.store_id) + ' ' + self.name


@python_2_unicode_compatible
class Key(models.Model):
    keynest_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    property_id = models.CharField(max_length=200, null=True)
    status = models.TextField(null=True)

    store_name = models.TextField(null=True)
    store_address = models.TextField(null=True)
    store_time = models.TextField(null=True)

    def __str__(self):
        return str(self.keynest_id) + ' ' + self.name
