# Generated by Django 4.2 on 2023-04-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_project_user_in_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images'),
        ),
    ]
