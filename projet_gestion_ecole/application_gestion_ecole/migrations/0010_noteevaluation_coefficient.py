# Generated by Django 4.2.5 on 2023-10-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_gestion_ecole', '0009_alter_noteevaluation_appreciation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteevaluation',
            name='coefficient',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]