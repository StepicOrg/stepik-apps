# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('about', '0005_auto_20170422_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='language',
            field=models.CharField(default='en', max_length=20),
        ),
    ]
