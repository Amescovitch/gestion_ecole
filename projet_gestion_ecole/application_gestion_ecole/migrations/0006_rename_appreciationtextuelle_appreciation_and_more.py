# Generated by Django 4.2.5 on 2023-10-14 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_gestion_ecole', '0005_anneeacademique_appreciationtextuelle_classeeleve_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppreciationTextuelle',
            new_name='Appreciation',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='appreciation_textuelle',
            new_name='appreciation',
        ),
    ]
