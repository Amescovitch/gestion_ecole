# Generated by Django 4.2.5 on 2023-10-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_gestion_ecole', '0008_noteevaluation_classe_noteevaluation_professeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteevaluation',
            name='appreciation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Appreciation',
        ),
    ]