# Generated by Django 3.2 on 2022-12-27 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20221227_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_image', to='bookings.club'),
        ),
    ]