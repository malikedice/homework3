# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
        migrations.AddField(
            model_name='director',
            name='director_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='film_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publisher',
            name='publisher_fav',
            field=models.BooleanField(default=False),
        ),
    ]
