# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_postpluginmodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postpluginmodel',
            name='title',
        ),
    ]
