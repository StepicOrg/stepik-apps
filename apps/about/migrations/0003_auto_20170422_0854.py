# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('about', '0002_about_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]