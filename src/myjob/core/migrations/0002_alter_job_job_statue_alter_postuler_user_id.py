# Generated by Django 4.0 on 2022-01-10 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Job_statue',
            field=models.CharField(choices=[('draft', 'en attente'), ('bad', 'refuser'), ('poster', 'ok'), ('close', 'fermer')], max_length=150),
        ),
        migrations.AlterField(
            model_name='postuler',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]