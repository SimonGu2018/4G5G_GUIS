# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-09 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0008_auto_20170109_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ueinfo',
            old_name='dl_state',
            new_name='dl_status',
        ),
        migrations.RenameField(
            model_name='ueinfo',
            old_name='ul_state',
            new_name='ul_status',
        ),
    ]
