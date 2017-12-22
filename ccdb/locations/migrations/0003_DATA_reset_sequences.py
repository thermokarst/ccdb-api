# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-18 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_DATA_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT setval('locations_region_id_seq', ("
            "SELECT MAX(id)+1 FROM locations_region), false)",

            "SELECT setval('locations_region_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('locations_site_id_seq', ("
            "SELECT MAX(id)+1 FROM locations_site), false)",

            "SELECT setval('locations_site_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('locations_municipallocation_id_seq', ("
            "SELECT MAX(id)+1 FROM locations_municipallocation), false)",

            "SELECT setval('locations_municipallocation_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('locations_studylocation_id_seq', ("
            "SELECT MAX(id)+1 FROM locations_studylocation), false)",

            "SELECT setval('locations_studylocation_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('locations_storagelocation_id_seq', ("
            "SELECT MAX(id)+1 FROM locations_storagelocation), false)",

            "SELECT setval('locations_storagelocation_id_seq', 1, false)"
        ),

    ]
