# Generated by Django 3.1 on 2020-09-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200927_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='birth_date',
            new_name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
