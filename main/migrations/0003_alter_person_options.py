# Generated by Django 4.0.1 on 2022-01-20 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_datatime_person_datetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-datetime']},
        ),
    ]