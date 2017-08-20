# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20170816_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bean',
            name='species',
        ),
        migrations.AlterField(
            model_name='bean',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]