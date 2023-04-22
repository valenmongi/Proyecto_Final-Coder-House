# Generated by Django 4.2 on 2023-04-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='project',
            name='assigned_to',
            field=models.CharField(default='Admin', max_length=100),
            preserve_default=False,
        ),
    ]