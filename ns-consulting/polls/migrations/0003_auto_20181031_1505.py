# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='percent',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
