# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170422_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
