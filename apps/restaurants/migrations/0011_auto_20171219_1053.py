# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20171219_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Grubber'),
        ),
    ]
