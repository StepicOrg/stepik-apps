# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_stepikuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepikuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stepik_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
