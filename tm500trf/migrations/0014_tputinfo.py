# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-01 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0013_ueinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TputInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('im', models.CharField(max_length=50)),
                ('ul', models.CharField(max_length=20)),
                ('dl', models.CharField(max_length=20)),
            ],
        ),
    ]
