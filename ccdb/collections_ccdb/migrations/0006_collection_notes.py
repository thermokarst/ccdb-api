# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-04 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0005_rename_flaws_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
