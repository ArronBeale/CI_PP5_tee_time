# Generated by Django 3.2 on 2022-12-26 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_club_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='course',
        ),
    ]
