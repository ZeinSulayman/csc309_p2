# Generated by Django 4.2.7 on 2023-11-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(default='Available', max_length=20),
        ),
    ]
