# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('matching', '0002_auto_20160128_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='pro', to=settings.AUTH_USER_MODEL),
        ),
    ]
