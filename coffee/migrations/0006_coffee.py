# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0005_powder_roast_syrup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('shots', models.IntegerField()),
                ('water', models.FloatField()),
                ('milk', models.BooleanField()),
                ('foam', models.FloatField()),
                ('extrainstructions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bean', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coffee.Bean')),
                ('powders', models.ManyToManyField(to='coffee.Powder')),
                ('roast', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coffee.Roast')),
                ('syrups', models.ManyToManyField(to='coffee.Syrup')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
