# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensions', '0007_category_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='extract_path',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]