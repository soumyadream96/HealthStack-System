# Generated by Django 4.0.6 on 2022-08-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_hospital_information_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
