# Generated by Django 4.0.6 on 2022-08-14 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_alter_appointment_appointment_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor_name',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_name',
            new_name='patient',
        ),
    ]
