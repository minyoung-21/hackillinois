# Generated by Django 5.0.2 on 2024-02-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_space_finder', '0004_buildingdetails_operating_end_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingdetails',
            name='operating_start_hours',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
