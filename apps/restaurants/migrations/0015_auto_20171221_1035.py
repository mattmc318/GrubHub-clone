# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0014_auto_20171221_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu_items',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
