# Generated by Django 4.1.5 on 2023-08-03 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_employee_department_transfer_incerement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 3, 16, 45, 17, 468843), null=True),
        ),
    ]