# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_plugins', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileWithBackgroundColor',
            new_name='FileLinkWithBackgroundColor',
        ),
    ]
