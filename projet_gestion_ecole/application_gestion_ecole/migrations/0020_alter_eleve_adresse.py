# Generated by Django 4.2.5 on 2023-11-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_gestion_ecole', '0019_alter_eleve_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='adresse',
            field=models.TextField(blank=True, default=''),
        ),
    ]
