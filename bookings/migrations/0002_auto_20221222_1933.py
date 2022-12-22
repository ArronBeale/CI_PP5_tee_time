# Generated by Django 3.2 on 2022-12-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='friendly_name',
        ),
        migrations.AddField(
            model_name='club',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
