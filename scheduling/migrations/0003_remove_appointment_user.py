# Generated by Django 5.1.4 on 2024-12-18 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
