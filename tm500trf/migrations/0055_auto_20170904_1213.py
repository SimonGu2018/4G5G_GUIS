# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-04 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0054_auto_20170904_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='cqi',
            field=models.CharField(default='N/A', max_length=10),
        ),
    ]
