# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='categories',
            field=models.ManyToManyField(related_name='extensions', to='main.Category'),
        ),
    ]
