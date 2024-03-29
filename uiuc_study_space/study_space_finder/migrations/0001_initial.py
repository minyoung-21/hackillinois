# Generated by Django 5.0.2 on 2024-02-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=200)),
                ('operating_hours', models.TimeField()),
                ('number_of_seats', models.IntegerField()),
                ('outlet_availability', models.BooleanField()),
                ('individual_room_availability', models.BooleanField()),
            ],
        ),
    ]
