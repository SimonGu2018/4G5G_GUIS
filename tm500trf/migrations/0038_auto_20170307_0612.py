# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-07 06:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0037_tm500'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PPPOE',
        ),
        migrations.DeleteModel(
            name='TM500',
        ),
    ]
