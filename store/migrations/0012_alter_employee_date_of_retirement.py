# Generated by Django 4.1.5 on 2023-08-03 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_employee_date_of_retirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 3, 18, 9, 34, 286215), null=True),
        ),
    ]
