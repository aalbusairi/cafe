# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170823_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
    ]
