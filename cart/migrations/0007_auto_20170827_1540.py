# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-27 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20170827_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coffee.Adress'),
        ),
    ]
