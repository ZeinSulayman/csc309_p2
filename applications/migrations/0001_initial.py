# Generated by Django 4.2.7 on 2023-11-13 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0003_remove_petshelter_user_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('hours_away_weekdays', models.CharField(max_length=255)),
                ('hours_away_weekends', models.CharField(max_length=255)),
                ('medical_history', models.CharField(max_length=255)),
                ('criminal_history', models.CharField(max_length=255)),
                ('previous_pet', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('available', 'Available'), ('pending', 'Pending'), ('withdrawn', 'Withdrawn'), ('denied', 'Denied'), ('accepted', 'Accepted')], default='available', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.pet')),
            ],
        ),
    ]
