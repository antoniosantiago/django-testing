# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20171123_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
