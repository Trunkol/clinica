# Generated by Django 3.2.9 on 2021-12-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telefone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone'),
        ),
    ]
