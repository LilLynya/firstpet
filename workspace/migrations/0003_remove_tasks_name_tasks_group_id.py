# Generated by Django 4.2.7 on 2024-03-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_rename_group_tasks_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='name',
        ),
        migrations.AddField(
            model_name='tasks',
            name='group_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]