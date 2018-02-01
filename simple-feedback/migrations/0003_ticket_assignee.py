# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-01 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple-feedback', '0002_auto_20180115_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]