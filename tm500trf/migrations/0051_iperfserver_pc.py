# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-16 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tm500trf', '0050_auto_20170816_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='IperfServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_ip', models.GenericIPAddressField()),
                ('username', models.CharField(max_length=30)),
                ('trafficip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_ip', models.GenericIPAddressField()),
                ('index', models.CharField(max_length=20)),
                ('ue_ip', models.GenericIPAddressField()),
                ('ulcmd', models.CharField(max_length=100)),
                ('dlcmd', models.CharField(max_length=100)),
                ('ulstatus', models.CharField(max_length=10)),
                ('dlstatus', models.CharField(max_length=10)),
                ('pcstatus', models.CharField(max_length=10)),
                ('uestatus', models.CharField(max_length=10)),
            ],
        ),
    ]
