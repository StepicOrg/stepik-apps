# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 09:05
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('about', '0003_auto_20170422_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
