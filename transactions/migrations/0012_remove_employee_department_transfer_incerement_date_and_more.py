# Generated by Django 4.1.5 on 2023-08-03 15:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_employee_date_of_retirement'),
        ('transactions', '0011_alter_employee_department_transfer_incerement_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_department_transfer',
            name='incerement_date',
        ),
        migrations.AddField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 3, 20, 50, 38, 777315), null=True),
        ),
        migrations.CreateModel(
            name='employee_increament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_basic', models.BigIntegerField()),
                ('new_basic', models.BigIntegerField()),
                ('description', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], max_length=120)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.department_type')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.employee')),
            ],
        ),
    ]
