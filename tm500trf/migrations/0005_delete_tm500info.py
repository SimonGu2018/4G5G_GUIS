# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-09 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0004_tm500info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TM500Info',
        ),
    ]
