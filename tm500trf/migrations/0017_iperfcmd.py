# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-01 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0016_auto_20170301_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='IperfCmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=5)),
                ('cmd', models.CharField(max_length=50)),
            ],
        ),
    ]