# Generated by Django 4.2 on 2023-04-22 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_rename_assigned_to_project_project_leader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_leader',
            new_name='project_manager',
        ),
    ]