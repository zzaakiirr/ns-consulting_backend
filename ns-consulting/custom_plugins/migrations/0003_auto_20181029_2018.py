# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 17:18
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_plugins', '0002_auto_20181017_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelinkwithbackgroundcolor',
            name='file_background_color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18, verbose_name='Цвет фона'),
        ),
        migrations.AlterField(
            model_name='linkwithbackgroundcolor',
            name='background_color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18, verbose_name='Цвет фона'),
        ),
    ]