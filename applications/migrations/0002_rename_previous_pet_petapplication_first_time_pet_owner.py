# Generated by Django 4.2.7 on 2023-11-17 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petapplication',
            old_name='previous_pet',
            new_name='first_time_pet_owner',
        ),
    ]
