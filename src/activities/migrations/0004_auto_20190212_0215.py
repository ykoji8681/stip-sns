# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-02-12 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20180302_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]