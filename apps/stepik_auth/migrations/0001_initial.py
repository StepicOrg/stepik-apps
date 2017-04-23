# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 20:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StepikUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.URLField(default='https://stepik.org/')),
                ('data', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stepik_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
