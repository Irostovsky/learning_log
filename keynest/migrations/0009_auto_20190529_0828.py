# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keynest', '0008_auto_20190529_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='full_status',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='status',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
