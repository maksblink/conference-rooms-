# Generated by Django 3.2.4 on 2021-06-17 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='room_id',
            new_name='room',
        ),
    ]
