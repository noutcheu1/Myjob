# Generated by Django 4.0 on 2022-01-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_job_date_debut_alter_job_date_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='metier',
            field=models.CharField(max_length=200),
        ),
    ]