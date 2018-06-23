# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-06 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IperfServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('port', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TM500Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_list', models.CharField(max_length=100)),
            ],
        ),
    ]