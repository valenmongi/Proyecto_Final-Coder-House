# Generated by Django 4.2 on 2023-04-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='publication',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='purchase',
            field=models.CharField(max_length=50),
        ),
    ]
