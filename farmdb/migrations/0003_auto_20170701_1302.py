# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmdb', '0002_auto_20170701_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='animal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmdb.Animal'),
        ),
        migrations.AlterField(
            model_name='slaughter',
            name='animal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmdb.Animal'),
        ),
    ]
