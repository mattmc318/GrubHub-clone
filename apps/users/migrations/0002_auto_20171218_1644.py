# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 22:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField(max_length=5)),
                ('phone_number', models.CharField(max_length=15)),
                ('cross_street', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_instructions', models.CharField(blank=True, max_length=255, null=True)),
                ('address_label', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users_addresses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddressManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='grubber',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='grubber',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='grubber',
            name='city',
        ),
        migrations.RemoveField(
            model_name='grubber',
            name='state',
        ),
    ]
