# Generated by Django 4.1.5 on 2023-08-07 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_remove_employee_dearness_allowance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 8, 4, 24, 40, 726122), null=True),
        ),
    ]