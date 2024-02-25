# Generated by Django 5.0 on 2023-12-30 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_delete_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
            ],
        ),
    ]
