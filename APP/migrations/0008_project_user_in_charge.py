# Generated by Django 4.2 on 2023-04-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_rename_project_leader_project_project_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user_in_charge',
            field=models.CharField(default='Admin', max_length=100),
            preserve_default=False,
        ),
    ]