# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0002_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
