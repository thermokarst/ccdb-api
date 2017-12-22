# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-18 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_DATA_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT setval('experiments_flaw_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_flaw), false)",

            "SELECT setval('experiments_flaw_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_experiment_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_experiment), false)",

            "SELECT setval('experiments_experiment_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_protocolattachment_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_protocolattachment), false)",

            "SELECT setval('experiments_protocolattachment_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_treatmenttype_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_treatmenttype), false)",

            "SELECT setval('experiments_treatmenttype_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_treatment_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_treatment), false)",

            "SELECT setval('experiments_treatment_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_treatment_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_treatment), false)",

            "SELECT setval('experiments_treatment_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_treatmentreplicate_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_treatmentreplicate), false)",

            "SELECT setval('experiments_treatmentreplicate_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('experiments_alivedeadcount_id_seq', ("
            "SELECT MAX(id)+1 FROM experiments_alivedeadcount), false)",

            "SELECT setval('experiments_alivedeadcount_id_seq', 1, false)"
        ),
    ]
