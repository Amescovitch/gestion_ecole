# Generated by Django 4.2.5 on 2023-10-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_gestion_ecole', '0016_alter_noteevaluation_appreciation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteevaluation',
            name='tranche_academique',
            field=models.CharField(default='', max_length=100),
        ),
    ]
