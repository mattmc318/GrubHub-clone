# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171218_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]
