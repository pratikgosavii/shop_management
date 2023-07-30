# Generated by Django 4.1.5 on 2023-07-29 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_delete_product_qr'),
        ('transactions', '0008_alter_project_material_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_qr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='static/qrcode/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.grade')),
                ('shelf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.godown')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.size')),
                ('thickness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.thickness')),
            ],
        ),
    ]