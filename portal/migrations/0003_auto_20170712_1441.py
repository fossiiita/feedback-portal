# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20170712_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='dean_or_director',
            field=models.BooleanField(default=False),
        ),
    ]