# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-02 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_auto_20170731_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='sharing_group',
            field=models.CharField(choices=[(b'chemical', b'Chemical'), (b'commercial', b'Commercial Facilities'), (b'communication', b'Communications'), (b'critical', b'Critical Manufacturing'), (b'dams', b'Dams'), (b'defense', b'Defense Industrial Base'), (b'emergency', b'Emergency Services'), (b'energy', b'Energy'), (b'financial', b'Financial Services'), (b'food', b'Food and Agriculture'), (b'government', b'Government Facilities'), (b'healthcare', b'Healthcare and Public Health'), (b'information', b'Information Technology'), (b'nuclear', b'Nuclear Reactors, Materials, and Waste'), (b'transport', b'Transportation Systems'), (b'water', b'Water and Wastewater Systems')], default=b'csc', max_length=128, null=True),
        ),
    ]